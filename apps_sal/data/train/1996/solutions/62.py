'''
Graph DFS brute force search
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # cycle detection
        # initial state 0, processing 1, eventual state 2
        n = len(graph)
        
        states = [0 for i in range(n)]
        
        def dfs(i):
            if states[i] != 0:
                return states[i]
            
            if not graph[i]:
                states[i] = 2
                return states[i]
            
            states[i] = 1
            eventual_state = 2
            for j in graph[i]:
                if states[j] == 0:
                    state_j = dfs(j)
                else:
                    state_j = states[j]
                eventual_state = min(state_j, eventual_state)
            
            states[i] = eventual_state
            return states[i]
        
        
        output = []
        for i in range(n):
            s = dfs(i)
            if s == 2:
                output.append(i)
        
        return sorted(output)
