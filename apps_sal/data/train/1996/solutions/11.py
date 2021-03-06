class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if not graph:
            return None
        n = len(graph)
        (out_degree, rgraph) = (collections.Counter(), collections.defaultdict(set))
        for (node, neighbors) in enumerate(graph):
            for nei in neighbors:
                out_degree[node] += 1
                rgraph[nei].add(node)
        q = collections.deque([x for x in range(n) if out_degree[x] == 0])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nei in rgraph[node]:
                if out_degree[nei] != 0:
                    out_degree[nei] -= 1
                    if out_degree[nei] == 0:
                        q.append(nei)
        ans.sort()
        return ans
