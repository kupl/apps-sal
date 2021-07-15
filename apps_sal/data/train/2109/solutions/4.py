import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    rr = []
    for _ in range(n):
        a,b = LI()
        t = a*b
        s = int(t ** 0.5)
        if t < 3:
            rr.append(0)
        elif a == b:
            if (a-1) * (b+1) < t:
                rr.append((a-1)*2)
            else:
                rr.append((a-1)*2-1)
        elif s*s == t:
            rr.append((s-1)*2-1)
        elif s*(s+1) < t:
            rr.append(s*2-1)
        else:
            rr.append((s-1)*2)


    return '\n'.join(map(str, rr))


print(main())



