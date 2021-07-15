def survivor(n):
    i=2
    while i<=n:
        if n%i==0:return False
        n-=n//i
        i+=1
    return True
