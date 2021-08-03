from string import ascii_lowercase as AL


def encode(s, key, n):
    a = "".join(dict.fromkeys(key + AL))
    d = {x: i for i, x in enumerate(a, 1)}
    r = []
    for x in s:
        if x in d:
            r.append(a[(d[x] + n - 1) % len(a)])
            n = d[x]
        else:
            r.append(x)
    return "".join(r)


def decode(s, key, n):
    a = "".join(dict.fromkeys(key + AL))
    d = {x: i for i, x in enumerate(a, 1)}
    r = []
    for x in s:
        if x in d:
            r.append(a[(d[x] - n - 1) % len(a)])
            n = d[r[-1]]
        else:
            r.append(x)
    return "".join(r)
