import re


def validate_number(string):
    return 'In with a chance' if re.match('^(07|\\+447)\\d{9}$', string.replace('-', '')) else 'Plenty more fish in the sea'
