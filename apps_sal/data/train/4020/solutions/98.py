import re


def validate_hello(greetings):
    r = 'hello ciao salut hallo hola ahoj czesc'.split()
    return len(re.findall('|'.join(r), greetings, re.I)) > 0
