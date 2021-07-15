from math import log
def compare_powers(n1,n2):
    a=n1[1]*log(n1[0])
    b=n2[1]*log(n2[0])
    if a==b: return 0
    if a>b: return -1
    return 1
