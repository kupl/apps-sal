def snap(a, b):
    (c, p, t) = (0, 1, [])
    while b:
        if p == 1:
            x = a.pop(0)
            if not t:
                t.append(x)
            elif t[-1] == x:
                c += 1
                a.extend(t + [x])
                t = [a.pop(0)]
            else:
                t.append(x)
        if p == -1:
            y = b.pop(0)
            if not t:
                t.append(y)
            elif t[-1] == y:
                c += 1
                a.extend(t + [y])
                t = []
            else:
                t.append(y)
        p *= -1
    return c
