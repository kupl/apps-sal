from itertools import cycle as c,islice as isl
sumDig_nthTerm=lambda ini,p,n:sum(map(int,str(ini+sum(list(isl(c(p),n-1))))))
