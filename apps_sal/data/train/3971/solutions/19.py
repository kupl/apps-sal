def tidyNumber(n):
    l=len(str(n))
    x=[int(x) for x in str(n)]
    return  all ( x[i+1]>=x[i]  for i in range(l-1) )

