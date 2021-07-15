validate_hello = lambda g: __import__('re').compile('(hello|ciao|salut|hallo|hola|ahoj|czesc)').search(g.lower()) is not None
