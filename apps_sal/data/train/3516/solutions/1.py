def present(x, y):
    if x == 'badpresent':
        return 'Take this back!'
    if x == 'goodpresent':
        return ''.join(chr(ord(i) + y) for i in x)
    if x == 'crap' or x == 'empty':
        return ''.join(sorted(x))
    if x == 'bang':
        return str(sum([ord(i) - y for i in x]))
    if x == 'dog':
        return "pass out from excitement {} times".format(y)
