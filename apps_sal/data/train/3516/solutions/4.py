def present(x, y):
    if x == 'badpresent':
        return 'Take this back!'
    if x == 'goodpresent':
        return ''.join(chr(ord(i) + y) for i in x)
    if x == 'crap':
        return 'acpr'
    if x == 'bang':
        return str(sum(ord(i) - y for i in x))
    if x == 'dog':
        return f'pass out from excitement {y} times'
    if x == 'empty':
        return x
