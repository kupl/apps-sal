import sys
from collections import defaultdict

# sys.stdin = open("ivo.in")
n = int(sys.stdin.readline())

h = defaultdict(set)
for iter in range(n):
  entry = sys.stdin.readline().rstrip() + "/"
  path_start = 7 + entry[7:].index('/')
  hostname = entry[:path_start]
  path = entry[path_start:]
  h[hostname].add(path)

res = defaultdict(list)
for k, v in h.items():
  res[frozenset(v)].append(k)

output = []
for v in res.values():
  if len(v) > 1:
    output.append(" ".join(v))

print(len(output))
for u in output:
  print(u)
