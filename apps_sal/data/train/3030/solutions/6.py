nb_dig = lambda n,d: sum(str(k**2).count(str(d)) for k in range(n+1))
