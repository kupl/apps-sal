i0 = 0.14849853757254047
r = 0.1353352832366127 #r is calculated from observation of different values of Cn, Geometric series is formed
def weight(n, w):
    return w*i0*(1-pow(r,n))/(1-r)
