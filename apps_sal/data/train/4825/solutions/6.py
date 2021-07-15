def decrypt(key):
    return ''.join(str(key.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz')
