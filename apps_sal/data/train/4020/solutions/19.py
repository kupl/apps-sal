def validate_hello(greetings):
    hellos = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for h in hellos:
        if h in greetings.lower():
            return True
    return False
