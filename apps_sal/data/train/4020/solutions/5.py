import re


def validate_hello(greetings):
    allowed_re = re.compile('(h[ae]llo)|(ciao)|(salut)|(hola)|(ahoj)|(czesc)')
    return bool(allowed_re.search(greetings.lower()))
