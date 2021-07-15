def century(year):
    S = str(year)
    L = len(str(year))
    if L == 2:
        return L - 1
    elif L == 3:
        return int(S[0]) + 1
    else:
        return int(S[:-2]) if S[-2:] == '00' else int(S[:-2]) + 1
