def decrypt(s):
    prev, c, r = 0, 0, []
    for x in reversed(s):
        d = int(x) - c - prev
        if d < 0:
            d += 10
            c = 1
        else:
            c = 0
        r.append(str(d))
        prev = d
    return 'impossible' if not prev else ''.join(r[::-1])
