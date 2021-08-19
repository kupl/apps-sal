class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        edge_value = collections.defaultdict()
        graph = collections.defaultdict(list)
        for (u, v) in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs1(u, parent):
            distance = 0
            vertex_num = 1
            for v in graph[u]:
                if v != parent:
                    (temp_dis, temp_ver) = dfs1(v, u)
                    distance += temp_dis
                    vertex_num += temp_ver
            if parent != -1:
                edge_value[parent, u] = (distance + vertex_num, vertex_num)
            return (distance + vertex_num, vertex_num)
        ans = [0] * N

        def dfs2(u, parent):
            nonlocal N
            total_dis = 0
            for v in graph[u]:
                (temp_dis, temp_ver) = edge_value[u, v]
                total_dis += temp_dis
            ans[u] = total_dis
            for v in graph[u]:
                if v != parent:
                    (temp_dis, temp_ver) = edge_value[u, v]
                    new_dis = total_dis - temp_dis + (N - temp_ver)
                    edge_value[v, u] = (new_dis, N - temp_ver)
                    dfs2(v, u)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans
