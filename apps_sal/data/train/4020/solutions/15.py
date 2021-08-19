import re


def validate_hello(greetings):
    return bool(re.search('(?i)(hello|ciao|salut|hallo|hola|ahoj|czesc)', greetings))
