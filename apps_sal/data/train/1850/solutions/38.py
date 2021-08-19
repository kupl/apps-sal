class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for i in range(N)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        cache = {}

        def dfs(i, exclude=-1):
            total = 0
            nodes_below_i = 0

            for j in adj[i]:
                if j != exclude:
                    try:
                        s, nodes_below_j = cache[j, i]
                    except KeyError:
                        s, nodes_below_j = dfs(j, i)

                    # 1 - to walk to node j
                    # nodes_below_j - for number of walks from i to j to reach all nodes below
                    # s - sum of all paths from j to all nodes below j
                    nodes_below_i += 1 + nodes_below_j
                    total += 1 + nodes_below_j + s

            cache[i, exclude] = total, nodes_below_i
            return total, nodes_below_i

        return [dfs(i)[0] for i in range(N)]
