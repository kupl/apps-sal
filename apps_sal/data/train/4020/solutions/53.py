import string


def validate_hello(greetings):
    HELLO_WORDS = {'hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc'}
    return any((x in HELLO_WORDS for x in greetings.translate(dict(((ord(char), None) for char in string.punctuation))).lower().split()))
