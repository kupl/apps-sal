s = {'hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'}


def validate_hello(g):
    return any(x in g.lower() for x in s)
