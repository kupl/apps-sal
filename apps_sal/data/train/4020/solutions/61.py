def validate_hello(greetings):
    hellos = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    greetings = greetings.lower()
    greetings = greetings.split(' ')
    for i in greetings:
        i = i.replace(',', '')
        i = i.replace('!', '')
        i = i.replace('.', '')
        i = i.replace('?', '')
        i = i.replace(';', '')
        i = i.replace(':', '')
        if i in hellos:
            return True
    return False
