def max_product(lst, n):
    return __import__('functools').reduce(int.__mul__, sorted(lst)[-n:])
