class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = {i:[] for i in range(1, N + 1)}
        for a, b in dislikes:
            edges[a].append(b)
            edges[b].append(a)
        
        groups = {}
        stack = []
        for i in range(1, N + 1):
            if i in groups:
                continue
            stack.append(i)
            groups[i] = 0
            while stack:
                cur = stack.pop()
                for dis in edges[cur]:
                    if dis not in groups:
                        stack.append(dis)
                        groups[dis] = groups[cur] ^ 1     
                    elif groups[dis] == groups[cur]:
                        return False
        return True
                       
                    
                     
                
                
                
                

