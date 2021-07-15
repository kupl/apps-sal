def validate_hello(text):
    text = text.lower()
    greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for hello in greetings:
        if hello in text:
            return True
    return False
