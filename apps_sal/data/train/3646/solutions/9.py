from math import factorial
fac = factorial  
subfac = lambda n: n * subfac(n-1)+(-1) ** n if not n == 0 else 1
def fixed_points_perms(n,k):
    if n < k: return 0
    return (fac(n)//(fac(n-k)*fac(k))) * subfac(n-k)
