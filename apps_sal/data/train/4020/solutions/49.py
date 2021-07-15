def validate_hello(greetings):
    #your code here
    hello_strings = ['hello',
                        'ciao',
                        'salut',
                        'hallo',
                        'hola',
                        'ahoj',
                        'czesc']
    #return True if (greetings.lower().find(s) != -1) else False for s in hello_strings
    for s in hello_strings:
        if greetings.lower().find(s) != -1:
            return True
    return False
