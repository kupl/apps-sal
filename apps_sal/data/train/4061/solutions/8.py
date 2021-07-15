from math import gcd

a=[7];g=[1];p=[];pn=[];ones=[1];anover=[]

for i in range(2,1000000):
    c = gcd(a[-1],i)
    g.append(c)
    a.append(a[-1]+c)
    if c!=1: 
        p.append(c)
        if c not in pn: pn.append(c)
        ones.append(ones[-1])
        anover.append(a[-1]/i)
    else:
        ones.append(ones[-1]+1)

def count_ones(n): return ones[n-1]
def max_pn(n): return max(pn[:n])
def an_over_average(n): return 3
