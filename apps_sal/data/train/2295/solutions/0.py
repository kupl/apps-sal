#from collections import deque,defaultdict
def printn(x): return print(x, end='')
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True  # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353


def ddprint(x):
    if DBG:
        print(x)


n = inn()
a = []
b = []
xb = 10**9 + 1
for i in range(n):
    aa, bb = inm()
    a.append(aa)
    b.append(bb)
    if aa > bb and xb > bb:
        xb = bb
        xi = i
if n == -2 and a[0] == 1:
    3 / 0
print(0 if xb > 10**9 else sum(a) - b[xi])
