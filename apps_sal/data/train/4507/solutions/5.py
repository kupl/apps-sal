def endless_string(stg, i, l):
    ls = len(stg)
    stg = stg * (2 + abs(l) // ls)
    i = min(i, i + l) % ls + (l < 0)
    j = i + abs(l)
    return stg[i:j]
