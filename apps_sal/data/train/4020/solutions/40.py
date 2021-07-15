def validate_hello(greetings):
    greetings = greetings.lower()
    a = "hello ciao salut hallo hola ahoj czesc"
    a = a.split(" ")
    for x in a:
        if x in greetings:
            return True
    return False
