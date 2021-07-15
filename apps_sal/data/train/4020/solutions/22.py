def validate_hello(greetings):
    if (greetings.upper().find("HELLO") >= 0
        or greetings.upper().find("CIAO") >= 0
        or greetings.upper().find("HALLO") >= 0
        or greetings.upper().find("SALUT") >= 0
        or greetings.upper().find("HOLA") >= 0
        or greetings.upper().find("AHOJ") >= 0
        or greetings.upper().find("CZESC") >= 0):
        return True
    else:
        return False
