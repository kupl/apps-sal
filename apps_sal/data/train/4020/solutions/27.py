def validate_hello(g):
    return any(i.lower() in g.lower() for i in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'])
