import re
def validate_hello(greetings):
    return True if re.findall('hello|ciao|salut|hallo|hola|ahoj|czesc', greetings, re.IGNORECASE) else False
