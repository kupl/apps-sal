import heapq
def max_product(a):
    x = heapq.nlargest(2,a)
    return x[0]*x[1]
