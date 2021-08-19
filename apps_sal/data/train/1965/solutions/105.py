class Solution:

    class DisjointSet:

        def __init__(self, n):
            self.parents = [i for i in range(n + 1)]
            self.ranks = [0 for i in range(n + 1)]

        def parent(self, node):
            if self.parents[node] != node:
                self.parents[node] = self.parent(self.parents[node])
            return self.parents[node]

        def join(self, node1, node2):
            p1 = self.parent(node1)
            p2 = self.parent(node2)
            r1 = self.ranks[p1]
            r2 = self.ranks[p2]
            if r1 < r2:
                self.parents[p1] = p2
            elif r2 < r1:
                self.parents[p2] = p1
            else:
                self.parents[p1] = p2
                self.ranks[p1] += 1

        def is_connected(self, node1, node2):
            return self.parent(node1) == self.parent(node2)

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        graph = [dict() for i in range(n + 1)]
        for edge in edges:
            if edge[2] not in graph[edge[1]]:
                graph[edge[1]][edge[2]] = edge[0]
            elif edge[0] == 3:
                if graph[edge[1]][edge[2]] == 4:
                    ans += 2
                else:
                    ans += 1
                graph[edge[1]][edge[2]] = 3
            elif graph[edge[1]][edge[2]] == 3:
                ans += 1
                graph[edge[1]][edge[2]] = 3
            else:
                graph[edge[1]][edge[2]] = 4
        alice_dset = Solution.DisjointSet(n)
        print(ans)
        for i in range(1, n + 1):
            for (j, t) in list(graph[i].items()):
                if t == 3:
                    if not alice_dset.is_connected(i, j):
                        alice_dset.join(i, j)
                    else:
                        ans += 1
        bob_dset = copy.deepcopy(alice_dset)
        for i in range(1, n + 1):
            for (j, t) in list(graph[i].items()):
                print((i, j, t))
                if t == 1 or t == 4:
                    if not alice_dset.is_connected(i, j):
                        alice_dset.join(i, j)
                    else:
                        ans += 1
                if t == 2 or t == 4:
                    if not bob_dset.is_connected(i, j):
                        bob_dset.join(i, j)
                    else:
                        ans += 1
        for i in range(1, n):
            if not bob_dset.is_connected(i, i + 1) or not alice_dset.is_connected(i, i + 1):
                return -1
        return ans
