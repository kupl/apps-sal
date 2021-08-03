def string_hash(s: str) -> int:
    a = sum(ord(c) for c in s)
    n = s.count(' ')
    b = ord(s[-1]) - ord(s[0]) if s else 0
    c = (a | b) & (~a << 2)
    d = c ^ ((n + 1) << 5)
    return d
