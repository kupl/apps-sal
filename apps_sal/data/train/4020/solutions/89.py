import re

def validate_hello(greetings):
    pattern = r'(h([ae]llo|ola)|c(iao|zesc)|salut|ahoj)'
    return bool(re.search(pattern, greetings, re.IGNORECASE))
