from math import gcd
def gcd_matrix(a,b):
    return round(sum(sum(gcd(i,j) for j in b) for i in a)/(len(a)*len(b)),3)
