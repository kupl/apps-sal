def unused_digits(*args):
    s = ''.join(map(str, args))
    return ''.join((str(i) for i in range(0, 10) if str(i) not in s))
