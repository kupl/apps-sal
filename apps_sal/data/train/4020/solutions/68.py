import re


def validate_hello(greetings):
    patterns = ["hello", "ciao", "salut", 'hallo', 'hola', "ahoj", 'czesc']
    catcher = re.findall(r'\w+', greetings.lower())
    for i in catcher:
        if i in patterns:
            return True
    return False
