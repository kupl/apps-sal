from math import factorial
def nth_perm(n,d):
    a=list(range(d))
    i=d-1
    r=''
    while(i>=0):
        b=(n-1)//factorial(i)
        r+=str(a[b])
        a.remove(a[b])
        n-=b*factorial(i)
        i-=1
    return r
