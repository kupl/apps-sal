def string_hash(s):
    a = sum(ord(c) for c in s)
    b = sum(ord(x) - ord(y) for x,y in zip(s[1:], s))
    c = (a | b) & ((~a) << 2)
    return c ^ ((s.count(" ") + 1) << 5)
