from collections import defaultdict


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def get_circle(comb):
            G = defaultdict(list)
            for t, u, v in edges:
                if t in comb:
                    G[u].append(v)
                    G[v].append(u)
            cnt = 0
            visited = set()
            for u in list(G.keys()):
                if u in visited:
                    continue
                visited.add(u)
                stack = [u]
                while stack:
                    cur = stack.pop()
                    for nei in G[cur]:
                        if nei not in visited:
                            visited.add(nei)
                            cnt += 1
                            stack.append(nei)
            return cnt

        type3 = get_circle((3,))
        if type3 == n - 1:
            return len(edges) - n + 1
        type2 = get_circle((2, 3))
        type1 = get_circle((1, 3))
        if type2 == type1 == n - 1:
            return len(edges) - (2 * n - 2 - type3)
        else:
            return -1
