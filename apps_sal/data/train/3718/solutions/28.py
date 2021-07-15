def divisors(n):
    sum=[]
    for i in range (1,n+1):
        if n%i==0:
            sum.append(i)
    return len(sum)
