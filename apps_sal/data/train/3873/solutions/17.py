from functools import reduce

def product(q):
    return reduce(int.__mul__, q)

def product_sans_n(q):
    if any(not x for x in q):
        return [product(q[0:i]+q[i+1:]) for i, x in enumerate(q)]
    else:
        n = product(q)
        return [n//x for x in q]
