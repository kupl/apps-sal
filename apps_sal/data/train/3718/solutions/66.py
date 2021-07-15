def divisors(n):
    count=0
    div=1
    while div<=n:
        if n%div==0:
            count +=1
            div+=1
        else:
            div+=1
    return count
