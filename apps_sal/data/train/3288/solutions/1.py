def solve(st,k):
    c=len(st)-k
    return int(max(st[i:i+c] for i in range(k+1)))
