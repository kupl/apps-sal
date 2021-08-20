import re


def validate_hello(greetings):
    return bool(re.findall('h[ae]llo|ciao|salut|hola|ahoj|czesc', greetings.lower()))
