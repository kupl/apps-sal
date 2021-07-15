from functools import reduce
from operator import mul
def get_num(a):
    a.sort()
    m = reduce(mul, [i ** a.count(i) for i in set(a)])
    total_d = reduce(mul, [a.count(i) + 1 for i in set(a)])
    return [m,total_d-1,a[0],m//a[0]]
