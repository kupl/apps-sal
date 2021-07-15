from functools import reduce
def tidyNumber(n):
    if n < 10:
        return True
    l = [str(n)[i] <= str(n)[i+1] for i in range(len(str(n))-1)]
    return reduce(lambda x, y:x & y, l)
