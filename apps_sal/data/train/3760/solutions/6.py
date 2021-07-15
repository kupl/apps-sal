roundRobin=lambda a,n,i:sum(min((a[i]+n*(i>=j)-1)//n*n,v)for j,v in enumerate(a))
