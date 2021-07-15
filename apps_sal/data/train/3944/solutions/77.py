def sum_triangular_numbers(n):
    num=1
    interval=2
    ls=list()
    while interval<=n:
        num=num+interval
        interval=interval+1
        ls.append(num)
    if n<0:
        return sum(ls)
    else:
        return sum(ls)+1
