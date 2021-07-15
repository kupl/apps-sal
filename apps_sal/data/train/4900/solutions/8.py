import math
def f(z, eps):
    tmp = math.log(eps, abs(z))
    return math.trunc(tmp) if tmp>0 else -1
