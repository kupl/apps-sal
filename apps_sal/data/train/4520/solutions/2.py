from heapq import nlargest
def max_product(a):
    x,y=nlargest(2,a)
    return x*y
