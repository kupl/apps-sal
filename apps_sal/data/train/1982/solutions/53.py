# from collections import defaultdict
# class Solution:
#     def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
#         graph = defaultdict(set)
        
#         for relation in dislikes:
#             graph[relation[0]].add(relation[1])
#             graph[relation[1]].add(relation[0])
            
class Solution:
    def possibleBipartition(self, N, dislikes):
        \"\"\"
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        \"\"\"
        if len(dislikes) < 3:
            return True
        
        graph = collections.defaultdict(list)
        color = {}    # -1 means red, 1 blue, 0 no color
        nodes = set()
        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)
            nodes.add(x)
            nodes.add(y)
                    
        for node in nodes:
            if node not in color:
                color[node] = 1
                q = collections.deque([node])
                while q:
                    cur = q.popleft()
                    cur_color = color[cur]
                    for nei in graph[cur]:
                        if nei not in color:
                            color[nei] = -cur_color
                            q.append(nei)
                        if color[nei] == cur_color:
                            return False
                        elif color[nei] == -cur_color:  # visited
                            continue
                        #color[nei] = -cur_color
                        
        return True
            
        
            
        
        
