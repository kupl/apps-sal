sumDig_nthTerm = lambda st, p, n:sum(map(int,str(st+sum(p)*((n-1)//len(p))+sum(p[:(n-1)%len(p)]))))
