import re


def validate_hello(greetings):
    multilingual_greetings = '(hello|ciao|salut|hallo|hola|ahoj|czesc)'
    return len(re.findall(multilingual_greetings, greetings, re.I)) > 0
