def encode(n, s):
    for i in range(n):
        s = ''.join(space(re(''.join([decore(e, n)for e in space(re(decore(s.replace(' ', ''), n)), ws(s)).split(' ')])), ws(s)))
    return str(n) + ' ' + s


def decode(s):
    n, s = s.split(' ', 1)
    n, sps = int(n), ws(s)
    for i in range(n):
        s = ''.join(space(re(decore(''.join([decore(e, -n)for e in s.split(' ')]), -n)), sps))
    return s


def space(stg, arr):
    for i in arr:
        stg.insert(i, ' ')
    return ''.join(stg)


def decore(code, key):
    l = (len(code) or 1)
    i = key % l
    return code[-i:] + code[:-i]


def ws(s): return [i for i, e in enumerate(s) if e == ' ']
def re(l): return [e for e in l]
