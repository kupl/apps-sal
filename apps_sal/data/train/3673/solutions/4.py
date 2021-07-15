
def totient(n):
    if not isinstance(n, int) or n<1:
        return 0
    factor=prime_factorization(n)
    up=1
    down=1
    for i in factor:
        up*=(i-1)
        down*=i
    return n*up//down
def prime_factorization(n):
    res=set()
    while n>1 and n%2==0:
        res.add(2)
        n//=2
    while n>1 and n%3==0:
        res.add(3)
        n//=3
    factor=5
    while factor*factor<=n:
        if n%factor==0:
            res.add(factor)
            n//=factor
            factor=5
        else:
            factor+=1
    if n>1:
        res.add(n)
    return res
