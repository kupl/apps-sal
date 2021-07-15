from functools import reduce as f
def max_product(lst, n):
    return f(lambda x,y: x * y, sorted(lst)[::-1][:n])
