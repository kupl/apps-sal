from functools import reduce

def product_array(num):
    s = reduce(int.__mul__, num)
    return [s/i for i in num]
