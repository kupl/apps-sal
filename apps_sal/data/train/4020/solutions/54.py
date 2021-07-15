def validate_hello(greetings):
    return any([i in greetings.lower() for i in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']])
