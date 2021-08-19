def unused_digits(*args):
    return ''.join(sorted(set('1234567890') - set(''.join((str(x) for x in args)))))
