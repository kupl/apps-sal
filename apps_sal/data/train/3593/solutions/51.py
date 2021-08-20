def capitalize(s, ind):
    if ind == []:
        return s
    else:
        return capitalize(s[:ind[0]] + s[ind[0]:].capitalize(), ind[1:])
