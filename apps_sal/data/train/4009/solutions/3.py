digits_average=f=lambda n:type(n)!=int and(len(n)>1and f([-~a+b>>1 for a,b in zip(n,n[1:])])or n[0])or f([int(e)for e in str(n)])
