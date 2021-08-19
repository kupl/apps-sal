import re


def validate(message):
    return re.match('^MDZHB( \\d\\d){2}\\d [A-Z]+( \\d\\d){4}$', message) != None
