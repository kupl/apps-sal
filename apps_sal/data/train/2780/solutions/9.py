def time(d, s, S):
    return round(d / (s + (-1) ** (S[0] > 'D') * int(S.split()[1])), 2)
