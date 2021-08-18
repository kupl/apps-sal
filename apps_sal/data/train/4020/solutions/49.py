def validate_hello(greetings):
    hello_strings = ['hello',
                     'ciao',
                     'salut',
                     'hallo',
                     'hola',
                     'ahoj',
                     'czesc']
    for s in hello_strings:
        if greetings.lower().find(s) != -1:
            return True
    return False
