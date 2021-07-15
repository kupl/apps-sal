def capitalize(s):
    i = 0
    ret = []
    for _ in range(2):
        alt = ''
        for e in s:
            alt += [e.upper(),e.lower()][i]
            i = not i
        ret.append(alt)
        i = [not i, i][len(alt)%2]
    return ret
