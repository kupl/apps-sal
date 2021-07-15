def max_product(lst, n):
    return __import__('functools').reduce(lambda x,y: x*y, __import__('heapq').nlargest(n, lst) )
    
    

