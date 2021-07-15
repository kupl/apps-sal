def validate_hello(greetings):
    greeting = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in greeting:
            if i in greetings.lower():
                return True
    return False
