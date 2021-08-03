class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        dislike_graph = collections.defaultdict(list)
        
        for dislike in dislikes:
            a, b = dislike[0], dislike[1]
            dislike_graph[a].append(b)
            dislike_graph[b].append(a)

        groups = [0]*(N+1)
        
        def can_split(cur, group):
            groups[cur] = group

            for neighbor in dislike_graph[cur]:
                if groups[neighbor] == group or \\
                (groups[neighbor] == 0 and not can_split(neighbor, -1*group)):
                    return False
            
            return True
        
        for i in range(1, N+1):
            if i not in dislike_graph:
                continue
            if groups[i] == 0 and not can_split(i, 1):

                return False
        
        return True
        
