def validate_hello(greetings):
    return any(w in greetings.lower() for w in ("hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"))
