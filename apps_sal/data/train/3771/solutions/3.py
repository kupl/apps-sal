from re import match


def validate_number(s):
    return ['Plenty more fish in the sea', 'In with a chance'][match('^(\\+44|0)7\\d{9}$', s.replace('-', '')) != None]
