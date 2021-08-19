class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = {}
        for (u, v, w) in edges:
            graph.setdefault(u, {})
            graph[u][v] = w
            graph.setdefault(v, {})
            graph[v][u] = w
        q = []
        HP = {}
        q.append([0, M])
        while q:
            (cur_node, cur_hp) = q.pop(0)
            if cur_node in HP and HP[cur_node] > cur_hp:
                continue
            HP[cur_node] = cur_hp
            if cur_node in graph:
                for next_node in graph[cur_node]:
                    weight = graph[cur_node][next_node]
                    next_hp = cur_hp - weight - 1
                    if next_hp < 0 or (next_node in HP and HP[next_node] > next_hp):
                        continue
                    q.append([next_node, next_hp])
        result = len(HP)
        for (u, v, w) in edges:
            uv = HP[u] if u in HP else 0
            vu = HP[v] if v in HP else 0
            result += min(uv + vu, w)
        return result
