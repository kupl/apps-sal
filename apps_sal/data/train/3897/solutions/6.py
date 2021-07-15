def solve(n,k):
    a  = list()
    for i in range(int(n/2)+1):
        a += [n-1-i,i]
    return a.index(k)
