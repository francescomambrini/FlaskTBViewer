# FlaskTBViewer

A very simple flask project to visualize treebanks from a CoNLL-U file.

## How does it work?

It just loads the [CoNLL-U](https://universaldependencies.org/format.html) file from the path specified in `settings.py`.

## How is the visualization made?

Simply, by converting the trees in the `.dot` format, then using [d3-graphviz](https://github.com/magjac/d3-graphviz) to render the image.

## The trees look familiar! Why is that?

I tried to replicate [Arethusa](https://github.com/alpheios-project/arethusa)'s beautiful colors!

