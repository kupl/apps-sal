def prime_maxlength_chain(n):
    p = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if p[i]:
            for j in range(i * 2, n + 1, i):
                p[j] = False
    pn = [i for (i, b) in enumerate(p) if b]
    ps = set(pn)
    maxl = [0, []]
    for l in range(6, len(pn)):
        if sum(pn[:l]) >= n:
            break
        for i in range(len(pn) - l):
            s = sum(pn[i:i + l])
            if s >= n:
                break
            elif s in ps:
                if maxl[0] < l:
                    maxl = [l, [s]]
                else:
                    maxl[1].append(s)
    return maxl[1]
