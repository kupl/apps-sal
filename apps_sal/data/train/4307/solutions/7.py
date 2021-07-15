def unused_digits(*args):
    return ''.join(sorted(set('0123456789') - {c for s in map(str, args) for c in s}))
