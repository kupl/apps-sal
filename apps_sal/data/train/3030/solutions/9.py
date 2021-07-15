nb_dig=lambda n,d:sum(str(i**2).count(str(d))for i in range(n+1))
