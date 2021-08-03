def validate_hello(greetings):
    msgs = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for msg in msgs:
        if msg in greetings.lower():
            return True
    return False
