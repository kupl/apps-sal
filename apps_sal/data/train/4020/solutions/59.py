def validate_hello(greetings):
    hey = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for x in hey:
        if x in greetings.lower():
            return True
    return False
