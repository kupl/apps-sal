def encode(s):
    return ''.join( str(1 - ord(c)%2) if c.isalpha() else c for c in s )
