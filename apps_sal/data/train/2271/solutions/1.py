#ARC097D Equals
def f(x):
    while q[x]>=0:
        x=q[x]
    return x
N, M = map(int, input().split())
p = list(map(int, input().split()))
q = [-1]*N
for _ in range(M):
    x, y = map(lambda x:f(int(x)-1), input().split())
    if x == y: continue
    elif x < y: x,y=y,x
    q[x] += q[y]
    q[y] = x
#方針:各木に分割、各木内の一致の最大数を足せばよい。
tree = [[] for n in range(N)]
for n in range(N):
    tree[f(n)].append(n)
    #print(f(n))
ans = 0
for n in range(N):
    ans += len(set(tree[n])&{p[i]-1 for i in tree[n]})
print(ans)
