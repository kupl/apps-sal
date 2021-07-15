class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # no out/ all out are safe state
        degree = [len(row) for row in graph]
        children = collections.defaultdict(list)
        
        for i,row in enumerate(graph):
            for j in row:
                children[j].append(i)
                
                
        seen = set()
        bfs = [i for i in range(len(degree)) if degree[i]==0]
        for val in bfs:
            if val in seen:
                continue
            seen.add(val)
            for child in children[val]:
                degree[child]-=1
                if not degree[child]:
                    bfs.append(child)
        return sorted(list(seen))
