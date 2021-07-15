def f(x):
    return ord(x)-ord("a")

class Bit:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
        self.el = [0]*(n+1)
        self.depth = n.bit_length() - 1

    def sum(self, i):
        """ 区間[0,i) の総和を求める """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1) )- 1
        return s

    def add(self, i, x):
        self.el[i] += x
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

class BitSet2:
    """ 座標圧縮が必要な場合 """
    def __init__(self, data, A=[]):
        """ BitSetに入り得る値を先読みした物を data に格納 """
        self.data = sorted(list(set(data)))
        self.n = len(self.data)
        self.p = Bit(self.n + 1)
        self.size = 0
        self.flip = 0
        self.code = {}
        self.decode = {}
        for i, b in enumerate(self.data):
            self.code[b] = i
            self.decode[i] = b
        for a in A:
            self.add(a)

    def add(self,x):
        self.p.add(self.code[x], 1)
        self.size += 1
        self.flip += self.size - self.p.sum(self.code[x]+1)

    def remove(self,x):
        self.p.add(x, -1)
        self.size -= 1

    def flip_counter(self):
        return self.flip

####################################################################################################

import sys
input = sys.stdin.readline

S=input().rstrip()
N=len(S)
P=[[] for _ in range(26)]
Q=[]
res=[-1]*N
for i, s in enumerate(S):
    P[f(s)].append(i)
for p in P:
    Np=len(p)
    for i in range(Np//2):
        Q.append((p[Np-1-i]-p[i],p[i],p[Np-1-i]))
    if len(p)%2:
        if res[N//2]!=-1 or N%2==0: print(-1); return
        res[N//2]=p[Np//2]
Q.sort(reverse=True)
for i,q in enumerate(Q):
    d,x,y=q
    res[i]=x
    res[N-1-i]=y

BS = BitSet2(res,res)
print(BS.flip_counter())
