def validate_hello(greetings):
    b = greetings.lower()
    for a in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']:
        if a in b:
            return True
    return False
