def validate_hello(g):
    st = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    g = g.lower()
    for i in st:
        if i in g:
            return True
    return False
