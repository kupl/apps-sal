def validate_hello(greetings):
    words = ['ciao', 'hello', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any((word in greetings.lower() for word in words))
