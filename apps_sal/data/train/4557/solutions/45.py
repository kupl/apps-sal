def row_weights(num):
    r = []
    for i in enumerate(num, start=1):
        r.append(i)
    d = dict(r)
    t1 = [d[i] for i in list(d.keys()) if i % 2 == 1]
    t2 = [d[i] for i in list(d.keys()) if i % 2 == 0]
    return sum(t1), sum(t2)
