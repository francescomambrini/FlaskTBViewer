from flask import render_template, redirect, url_for, request
from tbviewer import app
from tbeditor.editor import (parse_conllu_file, deps_to_dot, deprel_to_dot)


cpath = app.config['CONLLU']



def get_sent_by_id(sent_id, sent_list):
    res = None
    for s in sent_list:
        if s.metadata['sent_id'] == str(sent_id):
            return s
    return res


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/sent/<sent_id>/")
def display_sent(sent_id):
    return redirect(url_for("display_rel_sent", sent_id=sent_id, rel='deprel'))


@app.route("/sent/<sent_id>/<rel>")
def display_rel_sent(sent_id, rel):
    sents = parse_conllu_file(cpath)
    if rel not in ['deprel', 'deps']:
        rel = 'deprel'
    sent = get_sent_by_id(sent_id, sents)
    dot = 'digraph  {not -> found}'
    if sent:
        if rel == 'deps':
            dot = deps_to_dot(sent)
        else:
            dot = deprel_to_dot(sent)
    return render_template('sentence.html', dot=dot, sent_id=sent_id)


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        resp = request.form
        sent_id = resp.get('query')
        return redirect(url_for('display_rel_sent', sent_id=sent_id, rel='deprel'))
    else:
        return redirect(url_for("home"))
