from math import log2
def circle_slash(n):
    b=2**int(log2(n))
    return (n-b)*2+1
