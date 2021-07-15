def split_without_loss(s, sp):
    i,sp = sp.index("|"),sp.replace("|", "") ; r = s.split(sp)
    for k in range(len(r) - 1):
        r[k] += sp[:i] ; r[k + 1] = sp[i:] + r[k + 1]
    return [i for i in r if i]
