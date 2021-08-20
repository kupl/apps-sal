def decrypt(s):
    return ''.join((str(s.count(chr(c))) for c in range(97, 123)))
