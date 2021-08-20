def validate_hello(greetings):
    return max((i in greetings.lower() for i in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']))
