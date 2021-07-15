def round_it(n):
    l, r = map(len, str(n).split('.'))
    return [int(n+1),int(n),int(n+.5)][[l<r,l>r,r==l].index(True)]
