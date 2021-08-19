def shut_the_gate(farm):
    if not farm:
        return ''
    RA = []
    if farm[0] != '|' and farm[-1] != '|' and ('|' in farm):
        R = farm.rfind('|')
        L = farm.find('|')
        tmp = farm[R:] + farm[:L]
        if 'H' in tmp:
            farm = farm[:R] + farm[R:].replace('A', '.').replace('V', '.')
            farm = farm[:L].replace('A', '.').replace('V', '.') + farm[L:]
        if 'R' in tmp:
            farm = farm[:R] + farm[R:].replace('V', '.')
            farm = farm[:L].replace('V', '.') + farm[L:]
    res = ''
    L = len(farm)
    T = [e for e in range(L) if farm[e] == '|']
    if farm[0] != '|':
        T = [0] + T
    if farm[-1] != '|':
        T.append(L)
    idx = 0
    while True:
        if T[idx] == T[-1]:
            break
        S = T[idx]
        E = T[idx + 1]
        tmp = farm[S:E + 1]
        if 'H' in tmp:
            tmp = tmp.replace('A', '.').replace('V', '.')
        if 'R' in tmp:
            tmp = tmp.replace('V', '.')
        if tmp.count('|') <= 1:
            if 'H' in RA:
                tmp = tmp.replace('A', '.').replace('V', '.')
            if 'R' in RA:
                tmp = tmp.replace('V', '.')
            if 'H' in tmp:
                tmp = tmp.replace('H', '.')
                RA.append('H')
            if 'R' in tmp:
                tmp = tmp.replace('R', '.')
                RA.append('R')
            tmp = tmp.replace('C', '.')
        res += tmp[:-1] if E != T[-1] else tmp
        idx += 1
    return res
