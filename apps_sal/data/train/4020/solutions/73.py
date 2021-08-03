import re


def validate_hello(greetings):
    salute = 'hello|ciao|salut|hallo|hola|ahoj|czesc'
    return bool(re.search(salute, greetings, re.I))
