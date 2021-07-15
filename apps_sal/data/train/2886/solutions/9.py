from itertools import groupby
def find(s):
    a,b='',0
    m=0
    r=''
    for c,g in groupby(s):
        n=len(list(g))
        if b+n>m and b:
            r=a*b+c*n
            m=b+n
        a,b=c,n
    return r

