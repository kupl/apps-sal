def validate_hello(greetings):
    greeting = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in greeting:
        if s in greetings.lower():
            return True
    return False
