import re


def validate_number(string):
    if re.match('^(0|\\+44)7[0-9]{9}$', string.replace('-', '')):
        return 'In with a chance'
    else:
        return 'Plenty more fish in the sea'
