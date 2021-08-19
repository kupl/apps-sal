def validate_hello(greetings):
    i18n = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for word in i18n:
        if word in greetings.lower():
            return True
    return False
