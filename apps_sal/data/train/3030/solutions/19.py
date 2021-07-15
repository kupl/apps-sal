def nb_dig(n, d):
    l=[]
    for i in range(n+1):
        l.append(str(i**2))
    return ''.join(l).count(str(d))
