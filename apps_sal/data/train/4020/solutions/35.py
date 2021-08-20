def validate_hello(greetings):
    greetings = greetings.lower()
    if 'hello' in greetings or 'hallo' in greetings or 'ciao' in greetings or ('salut' in greetings) or ('hallo' in greetings) or ('hola' in greetings) or ('ahoj' in greetings) or ('czesc' in greetings):
        return True
    return False
