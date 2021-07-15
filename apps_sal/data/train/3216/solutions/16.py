from itertools import count
from scipy.special import lambertw
from math import log

def movie(a, b, c):
    if a>0:
        w = lambertw(-c**((a/b)+c/(1-c)+1)*log(c)/(c-1))
        x = (b*w-b*c*w-a*log(c)+a*c*log(c)-b*c*log(c))/(b*(c-1)*log(c))
        x = int(x.real+1)
        A = b*x
        B = a+b*sum(c**e for e in range(1,x+1))
        for i in range(x, x+5):
            print(i, A, int(B+1))
            if A>int(B+1):
                return i
            A += x
            B += b*c**i
    return 2
