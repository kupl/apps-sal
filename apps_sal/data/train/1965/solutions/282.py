
def kruskal(n, edges, person):
    parent = dict()
    rank = dict()

    def make_set(vertice):
        parent[vertice] = vertice
        rank[vertice] = 0

    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        if root1 != root2:
            if rank[root1] >= rank[root2]:
                parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]: rank[root2] += 1

    for i in range(1,n+1):
        make_set(i)
    minimum_spanning_tree = set()
    edges.sort(reverse=True)
    #print(edges)
    for i, edge in enumerate(edges):
        weight, vertice1, vertice2 = edge
        if weight != 3 and weight != person:
            continue
        #print(vertice1, find(vertice1), vertice2, find(vertice2))
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(i)
    count = 0
    for k, v in list(parent.items()):
        if k == v:
            count += 1
    return minimum_spanning_tree, count == 1

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        mst1, connected1 = kruskal(n, edges, 1)
        mst2, connected2 = kruskal(n, edges, 2)
        if not connected1 or not connected2:
            return -1
        return len(edges) - len(mst1.union(mst2))

