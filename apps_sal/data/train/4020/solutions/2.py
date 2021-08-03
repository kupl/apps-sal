import re


def validate_hello(greetings):
    return bool(re.search("h[ae]llo|ciao|salut|hola|ahoj|czesc", greetings.lower()))
