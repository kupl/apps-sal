def adfgx_encrypt(a, b):
    d = {x: (i // 5, i % 5) for (i, x) in enumerate(b)}
    if 'i' in d:
        d['j'] = d['i']
    else:
        d['i'] = d['j']
    return ''.join(('ADFGX'[y] + 'ADFGX'[z] for x in a for (y, z) in [d[x]]))


def adfgx_decrypt(a, b):
    it = iter(b)
    d = {x + y: next(it) for x in 'ADFGX' for y in 'ADFGX'}
    return ''.join((d[a[i:i + 2]] for i in range(0, len(a), 2)))
