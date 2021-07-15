def solve(n,k):
    d=int(2*n/(k*(k+1)))
    for i in range(d,0,-1):
        if n%i==0:
            d=i
            break
    if d==0:
        return []
    r=[d*i for i in range(1,k)]
    r.append(n-sum(r))
    return r
