def adfgx_encrypt(t, s):
    cr = 'ADFGX'
    r = ''
    for c in t:
        if c == 'j' and 'i' in s:
            c = 'i'
        p = s.index(c)
        r += cr[p // 5] + cr[p % 5]
    return r


def adfgx_decrypt(t, s):
    cr = 'ADFGX'
    r = ''
    for i in range(0, len(t), 2):
        r += s[cr.index(t[i]) * 5 + cr.index(t[i + 1])]
    return r
