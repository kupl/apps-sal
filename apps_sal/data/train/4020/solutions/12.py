import re

def validate_hello(greetings):
    return bool(re.search('ahoj|h[ea]llo|hola|czesc|ciao|salut', greetings, re.I))

