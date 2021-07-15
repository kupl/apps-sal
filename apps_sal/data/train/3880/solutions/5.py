def is_smooth(n):
    primes=set()
    n1=0
    while n1!=n:
        n1=n
        for p in {2,3,5,7}:
            if n%p==0:
                primes.add(p)
                n//=p
    if n!=1:return "non-smooth"
    return {2:"power of 2",3:"3-smooth",5:"Hamming number",7:"humble number"}[max(primes)]
