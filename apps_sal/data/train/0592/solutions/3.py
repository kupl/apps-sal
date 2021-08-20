D = {}


def g(s):
    if s in D:
        return D[s]
    vals = set()
    l = len(s)
    for i in range(l):
        for j in range(1, l + 1 - i):
            sub = s[i:i + j]
            if sub in DIC:
                vals.add(g(s[:i]) ^ g(s[i + j:]))
    i = 0
    while 1:
        if not i in vals:
            break
        i += 1
    D[s] = i
    return D[s]


T = int(input(''))
for t in range(T):
    s = input('')
    d_len = int(input(''))
    DIC = set()
    for i in range(d_len):
        DIC.add(input(''))
    D = {}
    print('Teddy' if g(s) else 'Tracy')
