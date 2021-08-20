def validate_hello(greetings):
    return any([i for i in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'] if i in greetings.lower()])
