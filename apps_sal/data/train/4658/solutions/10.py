def max_product(lst, n):
    return __import__('functools').reduce(lambda x,y: x*y,sorted(lst,reverse=True)[:n])
