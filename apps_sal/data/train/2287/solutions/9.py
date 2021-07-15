import sys
sys.setrecursionlimit(500000)

N = int(input())
E = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    E[a].append(b)
    E[b].append(a)
K = int(input())
L = [-float("inf")] * (N+1)
R = [float("inf")] * (N+1)
for _ in range(K):
    v, p = list(map(int, input().split()))
    L[v] = p
    R[v] = p

tour = []
def dfs(v, p):
    tour.append(v)
    for u in E[v]:
        if u!=p:
            dfs(u, v)
            tour.append(v)
dfs(v, 0)

l, r = L[v], R[v]
odd = p % 2
for v in tour[1:]:
    l -= 1
    r += 1
    odd = 1 - odd
    l_, r_ = L[v], R[v]
    if r_ != float("inf") and r_%2 != odd:
        print("No")
        return
    l = max(l, l_)
    r = min(r, r_)
    L[v] = l
    R[v] = r
for v in tour[-2::-1]:
    l -= 1
    r += 1
    odd = 1 - odd
    l_, r_ = L[v], R[v]
    l = max(l, l_)
    r = min(r, r_)
    if l > r:
        print("No")
        return
    L[v] = l
    R[v] = r
Ans = [-1] * (N+1)
print("Yes")
print(("\n".join(map(str, L[1:]))))

