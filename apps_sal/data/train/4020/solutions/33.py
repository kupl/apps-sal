def validate_hello(greetings):
    return True if sum(greetings.lower().find(i) for i in ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']) > -7 else False
