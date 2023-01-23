from bottle import route, run, template


@route("/")
def home():
    return "<b>Homepage</b>!"


@route("/hello/<name>")
def index(name):
    return template("<b>Hello {{name}}</b>!", name=name)


@route("/add/<a>/<b>")
def add(a, b):
    result = addCalc(a, b)
    return {"result": result}


def addCalc(a, b):
    """
        paramètre a : (int) un entier
        paramètre b : (int) un entier
        valeur renvoyée : (int) la somme de a et b.
    Exemples :
    >>> addCalc(3, 4)
    7

    >>> addCalc(10, 5)
    15

    >>> addCalc(-10, 5)
    -5
    """
    return int(a) + int(b)


run(host="localhost", port=8080, reloader=True)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
