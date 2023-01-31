import flask

app = flask.Flask("1")

@app.route("/<name>")
def a(name):
    return open(name,"rb").read()

app.run()