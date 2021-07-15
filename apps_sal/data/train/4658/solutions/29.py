from functools import reduce
max_product = lambda lst, n: reduce(lambda x,y: x*y, sorted(lst, reverse=True)[:n])
    

