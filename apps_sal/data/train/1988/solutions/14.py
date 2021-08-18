from collections import defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for x, y in red_edges:
            red[x].append(y)
        for x, y in blue_edges:
            blue[x].append(y)
        ans = []
        for i in range(n):
            visited = set()
            queue = [(0, 0, 0), (1, 0, 0)]
            level = -1
            visited.add((0, 0))
            visited.add((1, 0))
            while(queue):
                color, node, lvl = queue.pop(0)
                if(node == i):
                    level = lvl
                    break
                if(color == 0):
                    for neigh in red[node]:
                        if((1, neigh) not in visited):
                            queue.append((1, neigh, lvl + 1))
                            visited.add((1, neigh))
                elif(color == 1):
                    for neigh in blue[node]:
                        if((0, neigh) not in visited):
                            queue.append((0, neigh, lvl + 1))
                            visited.add((0, neigh))
            if(level == -1):
                ans.append(-1)
            else:
                ans.append(level)
            '''             
            visited = set()
            queue = [(1,0, 0)]
            red_level = -1
            while(queue):
                color, node, lvl = queue.pop(0)
                if(node == i):
                    red_level = lvl
                    break
                if(color == 0):
                    for neigh in red[node]:
                        if((1,node,neigh) not in visited):
                            queue.append((1,neigh, lvl+1))
                            visited.add((1,node,neigh))
                elif(color == 1):
                    for neigh in blue[node]:
                        if((0,node,neigh) not in visited):
                            queue.append((0, neigh, lvl+1))
                            visited.add((0,node,neigh))
            if(red_level == -1 and blue_level == -1):
                ans.append(-1)
            elif(red_level != -1 and blue_level == -1):
                ans.append(red_level)
            elif(red_level == -1 and blue_level != -1):
                ans.append(blue_level)
            else:
                ans.append(min(red_level,blue_level))'''

        return ans
