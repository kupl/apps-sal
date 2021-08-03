import re


def validate_hello(greetings):

    return any([greet in greetings.lower() for greet in 'hello ciao salut hallo hola ahoj czesc'.split()])
