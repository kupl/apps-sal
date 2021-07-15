class segment_tree_dual:
    def __init__(self, N, compose, funcval, ID_M=None):
        self.compose = compose
        self.ID_M = ID_M
        self.funcval = funcval

        self.height = (N-1).bit_length() #木の段数
        self.N0 = 1<<self.height #木の横幅 >= N
        self.laz = [self.ID_M]*(2*self.N0) #作用素の木
        self.val = None #値の配列

    #初期値の配列を作る
    def build(self,initial):
        self.val = initial[:]

    #laz[k] を子に伝える、k が一番下の場合は laz[k] を val に反映する
    def propagate(self,k):
        if self.laz[k] == self.ID_M: return;
        if self.N0 <= k:
            self.val[k-self.N0] = self.funcval(self.val[k-self.N0], self.laz[k])
            self.laz[k] = self.ID_M
        else:
            self.laz[(k<<1)  ] = self.compose(self.laz[(k<<1)  ],self.laz[k]);
            self.laz[(k<<1)+1] = self.compose(self.laz[(k<<1)+1],self.laz[k]);
            self.laz[k] = self.ID_M;
    
    # 遅延をすべて解消する
    def propagate_all(self):
        upto = self.N0 + len(self.val)
        for i in range(1,upto): self.propagate(i)

    # laz[k]およびその上に位置する作用素をすべて伝播
    def thrust(self,k):
        for i in range(self.height,-1,-1): self.propagate(k>>i)

    # 区間[l,r]に関数 f を作用
    def update(self, L,R,f):
        L += self.N0; R += self.N0+1
        """まず伝播させる（オペレータが可換なら必要ない）"""
        #self.thrust(L)
        #self.thrust(R-1)
        #登りながら関数 f を合成
        while L < R:
            if R & 1:
                R -= 1
                self.laz[R] = self.compose(self.laz[R],f)
            if L & 1:
                self.laz[L] = self.compose(self.laz[L],f)
                L += 1
            L >>= 1; R >>= 1
    
    # values[k] を取得。
    def point_get(self, k):
        res = self.val[k]
        k += self.N0
        while k:
            if self.laz[k] != self.ID_M:
                res = self.funcval(res, self.laz[k])
            k //= 2
        return res
    
    # values[k] = x 代入する
    def point_set(self, k): 
        self.thrust(k+self.N0)
        self.val[k] = x



# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

#x,y = map(int,readline().split())
from collections import deque
s = input()
lst = [deque() for _ in range(26)]
for i,c in enumerate(s):
    lst[ord(c)-97].append(i)

c = 0
for l in lst:
    if len(l)%2==1: c += 1
if c >= 2:
    print((-1))
    return

n = len(s)
L = 0
R = n-1
from operator import add
seg = segment_tree_dual(n, compose=add, funcval=add, ID_M=0)
seg.build([0]*n)

ans = 0
INF = 1<<30
for i in range(n//2):
    I = -1
    v = INF
    for idx in range(26):
        if lst[idx]:
            a,b = lst[idx][0], lst[idx][-1]
            d = a+seg.point_get(a)-i + n-1-i-(b+seg.point_get(b))
            #print(i,d,lst[idx],a+seg.point_get(a),(b+seg.point_get(b)))
            if d < v:
                I = idx
                v = d
    #print(v,I,lst[I],a,seg.point_get(a),n-1,(b+seg.point_get(b)))
    seg.update(0,lst[I].popleft(),1)
    seg.update(lst[I].pop(),n-1,-1)
    ans += v

print(ans)





