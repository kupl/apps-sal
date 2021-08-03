from collections import defaultdict


class Solution:
    def dfs1(self, n, edges):
        neighbours = dict()
        visited = set()
        for i in range(1, n + 1):
            neighbours[i] = set()
        for [t, u, v] in edges:
            if t in [1, 3]:
                neighbours[u].add(v)
                neighbours[v].add(u)

        def dfs(u):
            visited.add(u)
            for v in neighbours[u]:
                if v not in visited:
                    dfs(v)

        dfs(1)
        return len(visited) == n

    def dfs2(self, n, edges):
        neighbours = dict()
        visited = set()
        for i in range(1, n + 1):
            neighbours[i] = set()
        for [t, u, v] in edges:
            if t in [2, 3]:
                neighbours[u].add(v)
                neighbours[v].add(u)

        def dfs(u):
            visited.add(u)
            for v in neighbours[u]:
                if v not in visited:
                    dfs(v)

        dfs(1)
        return len(visited) == n

    def dfs3(self, n, edges):
        neighbours = dict()
        visited = dict()

        for i in range(1, n + 1):
            neighbours[i] = set()
        for [t, u, v] in edges:
            if t in [3]:
                neighbours[u].add(v)
                neighbours[v].add(u)

        def dfs(daddy, u):
            visited[u] = daddy
            for v in neighbours[u]:
                if v not in visited:
                    dfs(daddy, v)

        for i in range(1, n + 1):
            if i not in visited:
                dfs(i, i)

        cc_labels = set()
        cc_size = defaultdict(int)

        for u in visited:
            cc_labels.add(visited[u])
            cc_size[visited[u]] += 1

        num_cc = len(cc_labels)

        ret = 2 * (num_cc - 1)
        # print(\"num_cc=\", num_cc)
        # print(\"adding\", ret)
        for u in cc_size:
            # print(\"adding\", cc_size[u] - 1)
            ret += (cc_size[u] - 1)

        return ret

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        if not (self.dfs1(n, edges) and self.dfs2(n, edges)):
            return -1

        return len(edges) - self.dfs3(n, edges)
