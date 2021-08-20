def decrypt(test_key):
    return ''.join((str(test_key.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz'))
