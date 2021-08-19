def alphabet_position(s):
    return ' '.join((str(ord(c) - ord('a') + 1) for c in s.lower() if c.isalpha()))
