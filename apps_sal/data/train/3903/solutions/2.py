import re


def validate(message):
    return re.match(r'^MDZHB( \d\d){2}\d [A-Z]+( \d\d){4}$', message) != None
