class Solution:
\tdef findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
\t\tmap = collections.defaultdict(set)
\t\tfor f, t, w in edges:
\t\t\tmap[f].add((t, w))
\t\t\tmap[t].add((f, w))
\t\tstack = []
\t\tempty = -float(\"inf\")
\t\tres = 0
\t\tseen = []
\t\tfor i in range(n):
\t\t\tseen.append(collections.defaultdict(int))
\t\t\tstack.append((i, i, 0))
\t\t\tif i not in map:
\t\t\t\tempty = i
\t\tif empty != -float(\"inf\"):
\t\t\treturn empty
\t\twhile stack:
\t\t\tf, t, w = stack.pop()
\t\t\tfor a, b in map[t]:
\t\t\t\tif a not in seen[f] and w + b <= distanceThreshold and a != f:
\t\t\t\t\tseen[f][a] = w + b
\t\t\t\t\tstack.append((f, a, w + b))
\t\t\t\telif a in seen[f] and w + b <= seen[f][a] and a != f:
\t\t\t\t\tseen[f][a] = w + b
\t\t\t\t\tstack.append((f, a, w + b))
\t\tl = float(\"inf\")
\t\tfor k in range(len(seen)):
\t\t\tif len(seen[k]) <= l:
\t\t\t\tl = len(seen[k])
\t\t\t\tres = k
\t\treturn res
