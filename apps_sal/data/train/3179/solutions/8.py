def min_and_max(l,d,x):
    d_sum=lambda n:sum(map(int,str(n)))
    min=next(i for i in range(l,d+1) if d_sum(i)==x)
    max=next(i for i in range(d,l-1,-1) if d_sum(i)==x)
    return [min,max]
