def validate_hello(greetings):
    l = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    return any([True for i in l if i in greetings.lower()])
