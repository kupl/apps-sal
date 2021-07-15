from itertools import combinations as c
def solve(n,k):
    b=len(str(n))-k
    l=[''.join(i) for i in c(str(n),b)]
    return min(l)
