class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        nodes = reduce(lambda node, e: node[e[0]].extend(e[1]) or node, enumerate(graph), defaultdict(list))
        
        visited = set() 
        s = set()
        def dfs(i):
            if i in s:
                return False
            if i in visited:
                return True
            
            s.add(i)
            if not all(map(dfs, nodes[i])):
                return False
            s.remove(i)
            visited.add(i)
            return True 
        
        return [i for i in range(len(graph)) if dfs(i)]
