import re


def validate_number(s):
    if not s:
        return 'Plenty more fish in the sea'
    regex = '(?:-*)(0|\\+44)(7)((?:\\d-*){9})(?:-*)$'
    mo = re.match(regex, s)
    if mo:
        return 'In with a chance'
    else:
        return 'Plenty more fish in the sea'
