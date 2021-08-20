def validate_hello(greetings):
    hello_list = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    greetings = greetings.lower()
    for hello_str in hello_list:
        if hello_str in greetings:
            return True
    return False
