def max_product(lst, n):
    lst.sort(reverse=1)
    res=1
    for i in lst[:n]:
        res*=i
    return res

