def runoff(li):
    while all(li) and (not all((len(k) == 1 for k in li))):
        d = {l: 0 for k in li for l in k}
        for i in range(len(li)):
            d[li[i][0]] += 1
        m = min(d.values())
        li = [[j for j in i if d[j] != m] for i in li]
    return li[0][0] if li[0] else None
