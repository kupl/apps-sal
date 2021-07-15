def validate_hello(greetings):
    hellos = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    return any(hello in greetings.lower() for hello in hellos)
