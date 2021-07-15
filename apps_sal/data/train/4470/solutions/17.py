nb_year=n=lambda a,b,c,d,e=0:n(
a+a*b*.01+c
,b,c,d,e+1)if a<d else e
