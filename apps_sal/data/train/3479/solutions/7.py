part_const=p=lambda n,k,x,s=1:n!=x if k<2else sum(p(n-i,k-1,x,i)for i in range(s,n//k+1)if i!=x)
