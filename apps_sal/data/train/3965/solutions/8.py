def powerof4(n):
    if type(n)!=type(1):
        return False
    while n%4==0:
        n=n/4
    return n==1
