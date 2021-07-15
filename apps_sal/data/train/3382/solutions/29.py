def lowercase_count(s):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    return sum(x in ALPHABET for x in s)
