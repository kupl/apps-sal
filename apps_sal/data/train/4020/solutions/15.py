import re


def validate_hello(greetings):
    return bool(re.search(r'(?i)(hello|ciao|salut|hallo|hola|ahoj|czesc)', greetings))
