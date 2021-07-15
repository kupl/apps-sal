n = int(input())
g = [[] for i in range(n)]
for i in range(n-1):
    u,v = [int(i)-1 for i in input().split()]
    g[u].append(v)
    g[v].append(u)

leaf = [len(i)==1 for i in g]
root = -1
mx = n-1
for i in range(n):
    if leaf[i]:
        root = i
    leafs = 0
    for j in g[i]:
        if leaf[j]:
            leafs += 1
    if leafs > 1:
        mx -= leafs-1

stack = [(root, -1, 0)]
even = True
while len(stack)>0:
    i, j, d = stack.pop()
    if leaf[i] and d%2 == 1:
        even = False
        break
    for k in g[i]:
        if k != j:
            stack.append((k,i,d+1))
mn = 1 if even else 3

print(mn,mx)

