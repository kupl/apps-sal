def validate_hello(g):
    mes = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return 1 in list((g.lower().count(i) for i in mes))
