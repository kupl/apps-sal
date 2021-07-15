def string_hash(s):
    a = sum(ord(c) for c in s)
    b = ord(s[-1]) - ord(s[0]) if s else 0
    c = (a | b) & (~a << 2)
    return c ^ (32 * (s.count(' ') + 1))

