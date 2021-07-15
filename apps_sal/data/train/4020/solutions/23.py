def validate_hello(greetings):
    hello = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for greeting in hello :
        if greeting in greetings.lower() :
            return True
    return False
