def validate_hello(g):
    return __import__('re').compile('(hello|ciao|salut|hallo|hola|ahoj|czesc)').search(g.lower()) is not None
