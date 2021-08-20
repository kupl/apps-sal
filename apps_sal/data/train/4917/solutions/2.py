def validBraces(s, previous=''):
    while s != previous:
        (previous, s) = (s, s.replace('[]', '').replace('{}', '').replace('()', ''))
    return not s
