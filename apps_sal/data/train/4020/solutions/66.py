import re


def validate_hello(greetings):
    return any((w.lower() in {'hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'} for w in re.split('\\W', greetings)))
