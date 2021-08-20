greet = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']


def validate_hello(greetings):
    return any((w for w in greet if w in greetings.lower()))
