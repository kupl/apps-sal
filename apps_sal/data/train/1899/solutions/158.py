from itertools import product

class Solution(object):
    def getNeighbors(self, lst, x, y):
        # print(f'getting neighbors for {x}, {y}')
        numRows = len(lst)
        numCols = len(lst[0])
        
        for r, c in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= r < numRows and 0 <= c < numCols:
                yield r, c
    
    
    
    def dfs(self, r, c, A, seen, component):
        if A[r][c] and (r, c) not in seen:
            seen.add((r, c))
            component.add((r, c))

            for nei in self.getNeighbors(A, r, c):
                if A[nei[0]][nei[1]] and (nei[0], nei[1]) not in seen:
                    self.dfs(nei[0], nei[1], A, seen, component)

    def shortestBridge(self, A):
        \"\"\"
        :type A: List[List[int]]
        :rtype: int
        \"\"\"
        R = len(A)
        C = len(A[0])
        components = []
        seen = set()
        
        for rIdx, row in enumerate(A):
            for cIdx, val in enumerate(row):
                if val and (rIdx, cIdx) not in seen:
                    component = set()
                    self.dfs(rIdx, cIdx, A, seen, component)
                    components.append(component)
        
        # print(components)
        source, target = components[0], components[1]
        print(f'source {source}, target {target}')
        
        queue = collections.deque([(node, 0) for node in source])
        
        visited = set(source)
        
        while queue:
            node, dist = queue.popleft()
            # print(f'node - {node}, distance - {dist}')
            
            visited.add(node)
            
            for x, y in self.getNeighbors(A, *node):
                # print(f'processing neighbor {x}, {y}')
                if (x, y) in target:
                    return dist
                if (x, y) not in visited:
                    # print(f'adding node {(x,y)} to the queue')
                    queue.append(((x, y), dist+1))
                    visited.add((x, y))
