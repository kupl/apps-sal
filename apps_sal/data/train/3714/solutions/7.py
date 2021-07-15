import re

def encoder(s):
    d, i, r = {"": 0}, 0, []
    while i < len(s):
        x = ""
        while i < len(s) - 1 and x + s[i] in d:
            x += s[i]
            i += 1
        if x + s[i] not in d:
            d[x + s[i]] = len(d)
            r.append((d[x], s[i]))
        else:
            r.append((d[x + s[i]], ""))
        i += 1
    return "".join(str(x) + y for x, y in r)

def decoder(s):
    a, r = [""], []
    for x, y in re.findall(r"(\d+)(\D*)", s):
        a.append(a[int(x)] + y)
    return "".join(a)
