def encrypt(s, k):
    return code(s, k)


def decrypt(s, k):
    return code(s, k, -1)


def code(text, key, m=1):
    (keys, r) = ([int(e) * m for e in str(key).rjust(3, '0')], [])
    for c in text:
        for (i, a) in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm,.']):
            if c in a:
                c = a[(a.index(c) + keys[i]) % len(a)]
        for (i, a) in enumerate(['QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM<>']):
            if c in a:
                c = a[(a.index(c) + keys[i]) % len(a)]
        r.append(c)
    return ''.join(r)
