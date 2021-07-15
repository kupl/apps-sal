def validate_hello(greetings):
    d=['hello','ciao','salut','hallo','hola','ahoj','czesc']
    for i in d:
        if i in greetings.lower():
            return True
    return False
