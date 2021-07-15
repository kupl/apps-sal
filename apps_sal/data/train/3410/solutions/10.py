def scratch(L):
    z=0
    for x in L:
        a,b,c,d=x.split()
        z+=int(d)*(a==b==c)
    return z
