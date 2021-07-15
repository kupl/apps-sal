import re

def validate_hello(greetings):
    return len(re.findall('hello|ciao|salut|hallo|hola|ahoj|czesc', greetings.lower())) > 0
