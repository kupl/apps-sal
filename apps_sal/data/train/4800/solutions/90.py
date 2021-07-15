def hotpo(n):
    count=0
    while n>1:
        if n%2==0:
            n=int(n/2)
            count=count+1
        else:
            n=(3*n)+1
            count=count+1
    return count
