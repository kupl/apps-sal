def encode(s):
    return ''.join((str(ord(x) - ord('a') + 1) if x.isalpha() else x for x in s.lower()))
