class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(N)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        dist_sum = [0 for  _ in range(N)]
        node_num = [1 for _ in range(N)]
        
        def post_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                
                post_order(n, node)
                node_num[node] += node_num[n]
                dist_sum[node] += dist_sum[n] + node_num[n]
                
        def pre_order(node, parent):
            for n in graph[node]:
                if n == parent:
                    continue
                
                dist_sum[n] = dist_sum[node] - node_num[n] + (N - node_num[n])
                pre_order(n, node)

        
        post_order(0, -1)
        pre_order(0, -1)
        return dist_sum

