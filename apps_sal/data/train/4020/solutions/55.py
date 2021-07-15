def validate_hello(greetings):
    hello = ('hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc')
    return True if any([x in greetings.lower() for x in hello]) else False
