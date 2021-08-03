import re


def validate_hello(greetings):
    return bool(re.search('(?i)hello|ciao|hola|hallo|salut|czesc|ahoj', greetings))
