def list_squared(m, n):
    result=[]
    divisors=set()
    for i in range(m,n+1):
        a=1
        b=i/a
        divisors.clear()
        while a<=b:
            if b.is_integer():
                divisors.update((a,int(b)))
            a+=1
            b=i/a
        sqsum=sum(d**2 for d in divisors)
        if (sqsum**0.5).is_integer():
            result.append([i,sqsum])
    return result
            

