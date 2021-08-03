def levenshtein(s, t):
    v = range(len(t) + 1)
    for i, si in enumerate(s):
        w = [i + 1]
        for j, tj in enumerate(t):
            w.append(min(w[j] + 1, v[j + 1] + 1, v[j] + (si != tj)))
        v = w
    return w[-1]
