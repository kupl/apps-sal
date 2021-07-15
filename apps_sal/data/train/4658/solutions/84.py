def max_product(lst, n):
    from functools import reduce
    lst=[i for i in sorted(lst,reverse=True)[:n]]
    return reduce(lambda x,y:x*y,lst)
