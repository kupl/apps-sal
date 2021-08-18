def validate_hello(greetings):
    hello_strings = ['hello',
                     'ciao',
                     'salut',
                     'hallo',
                     'hola',
                     'ahoj',
                     'czesc']

    return any(s in greetings.lower() for s in hello_strings)
