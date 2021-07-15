def validate_hello(greetings):
    l = ['hello','ciao','salut','hallo','hola','ahoj','czesc']
    return any(i in greetings.lower() for i in l)
