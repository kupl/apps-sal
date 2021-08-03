def add(l):
    try:
        t = [l[0]]
        for i, j in enumerate(l[1:]):
            t.append(t[i] + j)
        if sum(l) % 1 != 0 or sum(t) % 1 != 0 or type(l) != list:
            return 'Invalid input'
        return t
    except:
        return 'Invalid input'
