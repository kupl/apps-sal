def decrypt(test_key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for n in alpha:
        s += str(test_key.count(n))
    return s
