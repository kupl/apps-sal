class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        def dfs(node):
            nodes.add(node)
            for i in range(len(graph[node])):
                if i not in nodes and graph[node][i] == 1:
                    dfs(i)
        
        rank, initial = collections.defaultdict(list), set(initial)
        for node in initial:
            nodes = set()
            dfs(node)
            #print(\"For initial node:\", node, \"the set is:\", nodes, 
            #     \"intersection is:\", sorted(nodes & initial))
            if len(nodes & initial) == 1:
                rank[len(nodes)].append(node)
        #print(\"Rank is:\", rank)
        return rank[max(rank)][0] if rank else min(initial)

