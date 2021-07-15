def string_hash(s):
    a = sum(ord(c) for c in s)
    b = sum(ord(b) - ord(a) for a, b in zip(s, s[1:]))
    c = (a | b) & (~a << 2)
    return c ^ (32 * (s.count(" ") + 1))

