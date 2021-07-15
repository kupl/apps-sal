def validate_hello(greetings):
    item = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    check = False
    for i in item:
        if i in greetings.lower():
            check = True
    return check            
