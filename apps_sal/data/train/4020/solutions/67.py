def validate_hello(greetings):
    p = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in p:
        if i in greetings.lower():
            return True
    return False
