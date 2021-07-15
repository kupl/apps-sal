max_product = lambda lst, n: __import__('functools').reduce(lambda x,y: x*y, sorted(lst, reverse=True)[:n])    
