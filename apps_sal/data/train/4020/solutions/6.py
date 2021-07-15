def validate_hello(greetings):
    check = False
    greeting = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for x in greeting:
        if x in greetings.lower():
            check = True
    return check
