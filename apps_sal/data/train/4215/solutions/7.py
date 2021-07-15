count_number=lambda n,x:sum(x-n*r<=x%r<1for r in range(1,n+1))
