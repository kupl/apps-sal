class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def make_graph(dislikes):
            graph = defaultdict(list)
            for dl in dislikes:
                graph[dl[1]].append(dl[0])
                graph[dl[0]].append(dl[1])
            return graph
        
        graph = make_graph(dislikes)
        color = {}
        
        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c^1) for nei in graph[node])
        return all(dfs(node) for node in range(1, N+1) if node not in color)
    
        for i in range(1, N+1):
            if i in visited:
                continue
            visited[i] = 'red'
            stack = [[i, visited[i]]]
            
         
            while stack:
                num, pos = stack.pop(0)
                for next_num in graph[num]:
                    if next_num in visited:
                        if visited[next_num] == pos:
                            print((next_num, num, pos))
                            return False
                    else:
                        if pos == 'blue': 
                            next_pos = 'red' 
                        else:
                            next_pos = 'blue' 
                        visited[next_num] = next_pos
                        stack.append([next_num, next_pos])
        return True
                        
                
                    
            
            

