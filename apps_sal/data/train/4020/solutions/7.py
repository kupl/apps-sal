import re
check = re.compile('hello|ciao|salut|hallo|hola|ahoj|czesc', re.IGNORECASE).search


def validate_hello(greetings):
    return bool(check(greetings))
