maxi = 12001
res = [2*maxi]*maxi
def rec(p, s, c, x):
    k = p - s + c
    if k >= maxi: return
    res[k] = min(p, res[k])
    [rec(p*i, s+i, c+1, i) for i in range(x, 2*maxi//p + 1)]
rec(1, 1, 1, 2)

def productsum(n):
    return sum(set(res[2:n+1]))
