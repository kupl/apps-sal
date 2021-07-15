from functools import reduce
def get_chance(n,x,a):
    return round(reduce(lambda x,y:x*y,((n-x-i)/(n-i) for i in range(a))),2)
