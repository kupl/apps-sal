def validate_hello(greetings):
    dic = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in dic:
        if greetings.lower().find(i) != -1:
            return True
    return False
