# cook your dish here
n = int(input())
edges = []
for i in range(n-1):
 a, b, c = map(int, input().strip().split())
 edges.append((c, a-1, b-1))
edges.sort()

parent = [-1]*n
def find(n):
 if parent[n] < 0:
  return n
 else:
  pt = find(parent[n])
  parent[n] = pt
  return pt

total = 0
num = 0
den = 0
for c, a, b in edges:
 a = find(a)
 b = find(b)
 assert a != b
 total += c
 num += parent[a] * parent[b] * c
 den += parent[a] * parent[b]
 if parent[a] > parent[b]:
  parent[b] += parent[a]
  parent[a] = b
 else:
  parent[a] += parent[b]
  parent[b] = a

print("%.11f" % (total - num / den))
