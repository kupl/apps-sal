import re


def validate_hello(greetings):
    print(greetings.lower())
    words = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for i in words:
        if bool(re.match('.*' + i + '.*', greetings.lower())):
            return True
    return False
