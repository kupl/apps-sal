def validate_hello(greetings):
    greets = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in greets:
        if i in greetings.lower():
            return True

    return False
