def performant_smallest(lst, n):
    c = [0] * 201
    for itm in lst:
        c[itm + 100] += 1
    (res, sm) = ([0] * n, 0)
    for k in range(201):
        sm += c[k]
        if sm >= n:
            c[k] += n - sm
            break
    sm = 0
    for itm in lst:
        v = itm + 100
        if v <= k and c[v] > 0:
            res[sm] = itm
            sm += 1
            c[v] -= 1
        if sm == n:
            break
    return res
