int_diff=lambda l,n:sum(n==abs(a-b)for i,a in enumerate(l)for b in l[:i])
