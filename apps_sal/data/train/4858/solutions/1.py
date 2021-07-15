from functools import lru_cache

@lru_cache(maxsize = None)
def john_value(n):
    if n == 0:
        return 0
    return n - ann_value(john_value(n - 1))
    
@lru_cache(maxsize = None)
def ann_value(n):
    if n == 0:
        return 1
    return n - john_value(ann_value(n - 1))

def ann(n):
    return [ann_value(x) for x in range(n)]

def john(n):
    return [john_value(x) for x in range(n)]

def sum_john(n):
    return sum(john(n))
    
def sum_ann(n):
    return sum(ann(n))
