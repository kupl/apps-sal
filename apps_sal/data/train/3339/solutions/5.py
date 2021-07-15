def mystery(n):
    while n>0 and n%2==0: n //= 2
    return [i for i in range(1,n+1,2) if n%i==0]
