def wheat_from_chaff(a):
    r, i, l = [[i, j] for i, j in enumerate(a) if j < 0], 0, len(a)
    for i in range(len(a)):
        if a[i] > 0:
            if not r:
                break
            r_ = r.pop()
            if r_[0] < i:
                break
            a[i], a[r_[0]] = r_[1], a[i]
    return a
