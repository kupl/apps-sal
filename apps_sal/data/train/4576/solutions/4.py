from fractions import gcd
def gcd_matrix(a,b):
    l = [gcd(i, j) for j in b for i in a]
    return round(sum(l)/len(l), 3)
