import re


def encoder(s):
    d, out, it = {}, [], iter(s)
    for c in it:
        i, k = 0, c
        while k in d:
            i, c = d[k], next(it, '')
            if not c:
                break
            k += c
        d[k] = len(d) + 1
        out.append(f'{i}{c}')
    return ''.join(out)


def decoder(s):
    d = ['']
    for m in re.finditer(r'(\d+)(\D?)', s):
        d.append(d[int(m[1])] + m[2])
    return ''.join(d)
