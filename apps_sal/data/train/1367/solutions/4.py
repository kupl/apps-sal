n = int(input())
size = {}
parent = {}

for i in range(1,n+1):
 size[i] = 1
 parent[i] = i

def find(a):
 if parent[a]==a:
  return a
 parent[a] = find(parent[a])
 return parent[a]

edges = []

for i in range(n-1):
 edges.append(list(map(int,input().split())))

edges.sort(key = lambda x:x[2])

c = 0
s = 0
t = 0

for i in range(n-1):
 a = find(edges[i][0])
 b = find(edges[i][1])
 c += edges[i][2]
 s += size[a]*size[b]*edges[i][2]
 t += size[a]*size[b]
 if size[a]>size[b]:
  size[a] += size[b]
  parent[b] = a
 else:
  size[b] += size[a]
  parent[a] = b

print("%.6f" % (c - float(s)/t))

