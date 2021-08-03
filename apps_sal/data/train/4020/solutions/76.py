def validate_hello(greetings):
    list = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    greetings = greetings.lower()
    for i in list:
        if greetings.find(i) >= 0:
            return True
    return False
