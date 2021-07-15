def capitalize(s,ind):
    s = list(s)
    last_indx = len(s) - 1
    for indx in ind:
        if indx > last_indx or indx < 0:
            pass
        else:
            s[indx] = s[indx].upper()
    return ''.join(s)


