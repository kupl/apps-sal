def hotpo(n):
    if n==1: return 0
    return hotpo(3*n+1 if n%2 else n/2)+1

