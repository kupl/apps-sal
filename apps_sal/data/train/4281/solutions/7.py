from math import asin,sin,pi
def tankvol(h,d,vt):
    a = pi-2*asin(1-2*h/d)
    return vt*(a-sin(a))/pi//2

