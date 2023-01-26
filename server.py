from functions import add
from bottle import route, run, template


@route("/hello/<name>")
def index(name):
    return template("<b>Hello My Dear {{name}}</b>!", name=name)


@route("/add/<a>/<b>")
@route("/add/<a>/<b>/")
def addition(a, b):
    return {"result": add(a, b)}


run(host="localhost", port=8080, reloader=True)
