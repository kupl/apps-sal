from re import search, IGNORECASE


def validate_hello(g):
    return bool(search("hello|ciao|salut|hallo|hola|ahoj|czesc", g, IGNORECASE))
