def validate_hello(greetings):
    greetings = greetings.lower()
    helloes = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for hello in helloes:
        if hello in greetings:
            return True
    return False
