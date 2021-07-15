def validate_hello(greetings):
    g=['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    gree=greetings.casefold()
    for i in g:
        if i in gree:
            return True
    return False
