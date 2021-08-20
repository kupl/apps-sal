import re


def validate_hello(greetings):
    res = re.search('hello|ciao|salut|hallo|hola|ahoj|czesc', greetings, re.IGNORECASE)
    return True if res else False
