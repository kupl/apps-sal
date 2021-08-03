def present(x, y):
    if x == 'badpresent':
        return "Take this back!"
    elif x == 'dog':
        return f'pass out from excitement {y} times'
    elif x in ['crap', 'empty']:
        return ''.join(sorted(x))
    elif x == 'goodpresent':
        return ''.join(map(lambda a: chr(ord(a) + y), x))
    else:
        return str(sum(map(lambda a: ord(a) - y, x)))
