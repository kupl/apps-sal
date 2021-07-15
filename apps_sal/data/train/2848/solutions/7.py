from itertools import combinations_with_replacement as cr
find=lambda a,n:sum(n==sum(c)for r in range(1,len(a)+1)for c in cr(a,r=r))
