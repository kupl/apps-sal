import re


def validate_hello(greetings):
    regex = '(hello|ciao|salut|hallo|hola|ahoj|czesc)'
    return True if re.search(regex, greetings.lower()) else False
