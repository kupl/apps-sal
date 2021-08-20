def string_hash(s):
    (a, b) = (sum((ord(x) for x in s)), sum((ord(y) - ord(x) for (x, y) in zip(s, s[1:]))))
    return (a | b) & ~a << 2 ^ 32 * (s.count(' ') + 1)
