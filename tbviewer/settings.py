import os

fpath = '~/bin/conllueditor/data/collu-editor-data/homer_ud/tlg0012.tlg001.perseus-grc1.1-6.tb.conllu'

CONLLU = os.path.expanduser(fpath)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
