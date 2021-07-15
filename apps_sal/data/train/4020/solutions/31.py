import re

def validate_hello(greetings):
    #print(greetings.lower())
    #print(re.search("[hello|ciao|salut|hallo|hola|ahoj|czesc]", greetings.lower()))
    return True if re.match(".*(hello|ciao|salut|hallo|hola|ahoj|czesc).*", greetings, re.IGNORECASE) else False
