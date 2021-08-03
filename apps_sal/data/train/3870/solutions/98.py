def solve(s):
    spaces = []
    count = 0
    for i in [c for c in s]:
        if i.isalpha():
            count += 1
        else:
            spaces.append(count)
            count += 1

    a = s.replace(" ", '')
    b = list(a)
    c = b[::-1]
    d = c
    for x in spaces:
        d.insert(x, ' ')
    e = ''.join(d)
    return e
