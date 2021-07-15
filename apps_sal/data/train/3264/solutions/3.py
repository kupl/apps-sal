from math import floor, log, pi

def count(n):
    return floor( ((n+0.5)*log(n) - n + 0.5*log(2*pi))/log(10) ) + 1
