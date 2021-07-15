def hotpo(n):
    if n==1 : return 0
    if n%2  : return 1+hotpo(3*n+1)
    else    : return 1+hotpo(n//2)
