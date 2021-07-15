from math import pi, log

def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in base pi with optional x decimals"""
    if n==0: return "0" if decimals==0 else "0."+"0"*decimals
    lexiconums='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res="" if n>0 else "-"
    n=abs(n)
    for i in range(int(log(n)/log(base)),-decimals-1,-1):
        divisor=base**i
        res+=lexiconums[int(n/divisor)]
        if i==0 and decimals>0: res+="."
        n%=divisor
    return res
