import re


def validate_number(s):
    for c in '-+':
        s = s.replace(c, '')
    return 'In with a chance' if re.match(r'^(07|447)\d{9}$', s) else 'Plenty more fish in the sea'
