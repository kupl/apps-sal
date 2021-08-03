def validate_hello(g):
    j = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any([x in g.lower() for x in j])
