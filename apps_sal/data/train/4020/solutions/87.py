def validate_hello(greetings):
    hello_list = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in hello_list:
        if i in greetings.lower():
            return True
    return False
