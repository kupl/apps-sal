def validate_hello(greetings):
    hellows = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    greetings = greetings.lower()
    result = False
    for x in hellows:
        if x in greetings:
            result = result or True
    return result
