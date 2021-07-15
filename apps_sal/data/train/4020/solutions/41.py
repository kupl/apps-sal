import re
def validate_hello(greetings):
    return bool(re.match(r".*(hello|ciao|salut|hallo|hola|ahoj|czesc).*",greetings,flags=re.IGNORECASE))
