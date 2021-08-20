def present(present, passes):
    if present == 'goodpresent':
        return ''.join((chr(ord(c) + passes) for c in present))
    elif present == 'crap' or present == '':
        return ''.join(sorted(present))
    elif present == 'bang':
        return str(sum(map(ord, present)) - passes * len(present))
    elif present == 'badpresent':
        return 'Take this back!'
    elif present == 'dog':
        return f'pass out from excitement {passes} times'
    else:
        return 'empty'
