import re


def validate_hello(greetings):
    return bool(re.search('hello|ciao|salut|hallo|hola|ahoj|czesc', greetings, re.I))
