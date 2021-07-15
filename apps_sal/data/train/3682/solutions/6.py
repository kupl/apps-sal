def string_constructing(a, s):
    T = a
    c, al = 1, 0
    while T != s:
        if al < len(T) and al < len(s) and T[al] == s[al]:
            al += 1
        elif al == len(T):
            T += a
            c += 1
        elif len(s) < len(T) or T[al] != s[al]:
            T = T[:al] + T[al + 1:]
            al = max(al - 1, 0)
            c += 1
    return c
