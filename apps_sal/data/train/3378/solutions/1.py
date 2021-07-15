def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s
