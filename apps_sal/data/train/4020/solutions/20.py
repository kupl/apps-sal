import re


def validate_hello(greetings: str) -> bool:
    """ Check if the string contains the word hallo in different languages. """
    return bool(re.search('(hello|ciao|salut|hallo|hola|ahoj|czesc)', greetings, re.I))
