import re


def validate_hello(greetings):
    return re.search(".*h[ae]llo|ciao|salut|hola|ahoj|czesc", greetings.lower()) is not None
