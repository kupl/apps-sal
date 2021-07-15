N, M = map(int, input().split())
p = list(map(int, input().split()))

p = [0] + p
par = list(range(N+1))

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
    
def unite(x, y):
    if find(x) != find(y):
        par[find(x)] = y
        
for _ in range(M):
    a, b = map(int, input().split())
    unite(a, b)
    
# for i in range(1, N+1):
#     find(i)

# print(p)    #
# print(par)  #

ans = 0
for i in range(1, N+1):
    if find(p[i]) == find(p[p[i]]):
        ans += 1
#         print(ans)  #
        
print(ans)
