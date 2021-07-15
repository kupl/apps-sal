k,solve=lambda n,p:n%p<1and-~k(n//p,p),lambda a:sorted(a,key=lambda n:(-k(n,3),k(n,2)))
