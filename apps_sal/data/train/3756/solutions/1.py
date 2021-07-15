f=lambda n:n>1and all(n%d for d in range(2,int(n**.5)+1))
goldbach_partitions=lambda n:[]if n%2else['%d+%d'%(p,n-p)for p in range(n//2+1)if f(p)*f(n-p)]
