from string import ascii_uppercase as up
from math import ceil
def new_numeral_system(num):
    n=up.index(num)
    n1=ceil(n/2)
    return list(f"{a} + {b}" for a,b in zip(up[:n1+1],up[n1:n+1][::-1]))
