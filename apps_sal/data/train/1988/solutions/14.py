from collections import defaultdict


class Solution:

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for (x, y) in red_edges:
            red[x].append(y)
        for (x, y) in blue_edges:
            blue[x].append(y)
        ans = []
        for i in range(n):
            visited = set()
            queue = [(0, 0, 0), (1, 0, 0)]
            level = -1
            visited.add((0, 0))
            visited.add((1, 0))
            while queue:
                (color, node, lvl) = queue.pop(0)
                if node == i:
                    level = lvl
                    break
                if color == 0:
                    for neigh in red[node]:
                        if (1, neigh) not in visited:
                            queue.append((1, neigh, lvl + 1))
                            visited.add((1, neigh))
                elif color == 1:
                    for neigh in blue[node]:
                        if (0, neigh) not in visited:
                            queue.append((0, neigh, lvl + 1))
                            visited.add((0, neigh))
            if level == -1:
                ans.append(-1)
            else:
                ans.append(level)
            '             \n            visited = set()\n            queue = [(1,0, 0)]\n            red_level = -1\n            while(queue):\n                color, node, lvl = queue.pop(0)\n                if(node == i):\n                    red_level = lvl\n                    break\n                #previous is blue\n                if(color == 0):\n                    for neigh in red[node]:\n                        if((1,node,neigh) not in visited):\n                            queue.append((1,neigh, lvl+1))\n                            visited.add((1,node,neigh))\n                #previous is red\n                elif(color == 1):\n                    for neigh in blue[node]:\n                        if((0,node,neigh) not in visited):\n                            queue.append((0, neigh, lvl+1))\n                            visited.add((0,node,neigh))\n            if(red_level == -1 and blue_level == -1):\n                ans.append(-1)\n            elif(red_level != -1 and blue_level == -1):\n                ans.append(red_level)\n            elif(red_level == -1 and blue_level != -1):\n                ans.append(blue_level)\n            else:\n                ans.append(min(red_level,blue_level))'
        return ans
