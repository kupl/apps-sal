class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for i in range(N)]
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        dist = [0 for i in range(N)]
        nums = [1 for i in range(N)]

        def post_order(node, parent):
            for i in graph[node]:
                if i == parent:
                    continue
                post_order(i, node)
                nums[node] += nums[i]
                dist[node] += dist[i] + nums[i]

        def pre_order(node, parent):
            for i in graph[node]:
                if i == parent:
                    continue
                dist[i] = dist[node] - nums[i] + N - nums[i]
                pre_order(i, node)

        post_order(0, -1)
        pre_order(0, -1)
        return dist
