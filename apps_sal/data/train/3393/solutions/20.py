div=lambda n:sum(set(sum([[i**2,(n//i)**2] for i in range(2,int(n**.5)+1) if not n%i],[]))) + n*n + int(n!=1)
d = {i: div(i) for i in range(10001)}   
list_squared=lambda a,b:[[i,d[i]] for i in range(a,b+1) if (d[i]**.5).is_integer()]
