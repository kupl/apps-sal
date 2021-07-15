import sys
readline = sys.stdin.readline
class UF():
    def __init__(self, num):
        self.par = [-1]*num
        self.weight = [0]*num
    def find(self, x):
        stack = []
        while self.par[x] >= 0:
            stack.append(x)
            x = self.par[x]
        for xi in stack:
            self.par[xi] = x
        return x
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.par[rx] > self.par[ry]:
                rx, ry = ry, rx
            self.par[rx] += self.par[ry]
            self.par[ry] = rx
            self.weight[rx] += self.weight[ry]
        return rx


N, K = list(map(int, readline().split()))
S = list(map(int, readline().strip()))

A = [[] for _ in range(N)]

for k in range(K):
    BL = int(readline())
    B = list(map(int, readline().split()))
    for b in B:
        A[b-1].append(k)

cnt = 0
T = UF(2*K)
used = set()
Ans = [None]*N
inf = 10**9+7
for i in range(N):
    if not len(A[i]):
        Ans[i] = cnt
        continue
    kk = 0
    if len(A[i]) == 2:    
        x, y = A[i]
        if S[i]:
            rx = T.find(x)
            ry = T.find(y)
            if rx != ry:
                rx2 = T.find(x+K)
                ry2 = T.find(y+K)
                sp = min(T.weight[rx], T.weight[rx2]) + min(T.weight[ry], T.weight[ry2])
                if x not in used:
                    used.add(x)
                    T.weight[rx] += 1
                if y not in used:
                    used.add(y)
                    T.weight[ry] += 1
                rz = T.union(rx, ry)
                rz2 = T.union(rx2, ry2)
                sf = min(T.weight[rz], T.weight[rz2])
                kk = sf - sp
        else:
            rx = T.find(x)
            ry2 = T.find(y+K)
            sp = 0
            if rx != ry2:
                ry = T.find(y)
                rx2 = T.find(x+K)
                sp = min(T.weight[rx], T.weight[rx2]) + min(T.weight[ry], T.weight[ry2])
                if x not in used:
                    used.add(x)
                    T.weight[rx] += 1
                if y not in used:
                    used.add(y)
                    T.weight[ry] += 1
                rz = T.union(rx, ry2)
                rz2 = T.union(rx2, ry)
                sf = min(T.weight[rz], T.weight[rz2])
                kk = sf - sp
    else:
        if S[i]:
            x = A[i][0]
            rx = T.find(x)
            rx2 = T.find(x+K)
            sp = min(T.weight[rx], T.weight[rx2])
            T.weight[rx] += inf
            sf = min(T.weight[rx], T.weight[rx2])
            kk = sf - sp
        else:
            x = A[i][0]
            rx = T.find(x)
            rx2 = T.find(x+K)
            sp = min(T.weight[rx], T.weight[rx2])
            T.weight[rx2] += inf
            if x not in used:
                used.add(x)
                T.weight[rx] += 1
            sf = min(T.weight[rx], T.weight[rx2])
            kk = sf-sp
    Ans[i] = cnt + kk
    cnt = Ans[i]            
print('\n'.join(map(str, Ans)))
            

