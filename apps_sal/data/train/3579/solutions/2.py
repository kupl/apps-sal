def choose(n,k):
    l = [max(k,n-k),min(k,n-k)]
    nu = 0 if k > n else 1
    de = 1
    for i in range(l[0]+1,n+1):
        nu *= i
    for i in range(1,l[1]+1):
        de *= i
    return int(nu/de)
