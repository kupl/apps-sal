class Solution:
\tdef minCostConnectPoints(self, points: List[List[int]]) -> int:
\t\tfrom    itertools   import  combinations
\t\tParent\t\t= {}
\t\tRank\t\t= {}
\t\tVertices\t= list(range(len(points)))
\t\tEdges\t\t= []

\t\tdef\tMakeGraph():
\t\t\tnonlocal\tpoints, Parent, Rank, Vertices, Edges
\t\t\tCombi\t= list(combinations(Vertices, 2))
\t\t\t
\t\t\tfor pair in Combi:
\t\t\t\tu, v\t= pair
\t\t\t\tnDist\t=\tabs(points[u][0] - points[v][0]) \\
\t\t\t\t\t+ abs(points[u][1] - points[v][1])
\t\t\t\tEdges.append((nDist, u, v))
\t\t\tEdges.sort()

\t\tdef MakeSet(v):
\t\t\tnonlocal\tParent, Rank
\t\t\tParent[v]\t= v
\t\t\tRank[v]\t\t= 0

\t\tdef FindRoot(v):
\t\t\tnonlocal\tParent
\t\t\tif Parent[v] != v:
\t\t\t\tParent[v] = FindRoot(Parent[v])

\t\t\treturn Parent[v]

\t\tdef Union(u, v):
\t\t\troot1 = FindRoot(v)
\t\t\troot2 = FindRoot(u)

\t\t\tif root1 != root2:
\t\t\t\t# 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋다.
\t\t\t\tif Rank[root1] > Rank[root2]:
\t\t\t\t\tParent[root2] = root1
\t\t\t\telse:
\t\t\t\t\tParent[root1] = root2

\t\t\t\t\tif Rank[root1] == Rank[root2]:
\t\t\t\t\t\tRank[root2] += 1

\t\tMakeGraph()
\t\tfor v in Vertices:
\t\t\tMakeSet(v)

\t\tnMinCost\t= 0
\t\tfor Edge in Edges:
\t\t\tnCost, u, v\t= Edge
\t\t\tif FindRoot(u) != FindRoot(v):
\t\t\t\tUnion(u, v)
\t\t\t\tnMinCost\t+= nCost
\t\t
\t\treturn  nMinCost
