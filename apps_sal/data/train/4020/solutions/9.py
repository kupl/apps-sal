def validate_hello(greetings):
    a=('hello','ciao','salut','hallo','hola','ahoj','czesc')
    for x in a:
        if x in greetings.lower():
            return True
    return False
