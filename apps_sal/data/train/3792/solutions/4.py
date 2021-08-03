def slogans(p, r):
    c = 0
    while r:
        t, f = p[:], r[0]
        x = t.find(f)
        t = t[x:]
        if t == r[:len(t)]:
            r = r[len(t):]
            c += 1
        else:
            x = 0
            while x < len(r):
                try:
                    x = t.find(f, 1)
                    t = t[x:]
                    if t == r[:len(t)]:
                        r = r[len(t):]
                        c += 1
                        break
                except:
                    break
    return c
