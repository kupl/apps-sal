
def find_parent(u):
    if par[u]!=u:
        par[u]=find_parent(par[u])
    return par[u]

n,k = list(map(int,input().split()))

l = []

par = [0]+[i+1 for i in range(n)]

g = []
rank = [1]*(n+1)

ans = 0
for i in range(k):
    a,b = list(map(int,input().split()))
    z1,z2 = find_parent(a),find_parent(b)
    if z1!=z2:
        par[z1] = z2
        rank[z2]+=rank[z1]
        ans+=1

print(k-ans)










