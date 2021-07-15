from functools import reduce, partial
from operator import mul
product = partial(reduce, mul) 

def maximum_product_of_parts(n):
    s = str(n)
    l = len(s)
    return max(product(map(int, (s[:i], s[i:j], s[j:]))) for i in range(1, l-1) for j in range(i+1, l))
