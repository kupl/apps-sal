from re import compile, search, I
LOL = compile('hello|ciao|salut|hallo|hola|ahoj|czesc', I)


def validate_hello(greeting):
    return bool(search(LOL, greeting))
