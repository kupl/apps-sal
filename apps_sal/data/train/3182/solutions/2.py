import math
def LDTA(n):
    if math.log10(n) == int(math.log10(n)): return None
    d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    c = n
    while 1:
        for i in str(c):
            d[int(i)] = 1
            if sum(d.values()) == 10:
                return int(i)
        c *= n
    return -1
