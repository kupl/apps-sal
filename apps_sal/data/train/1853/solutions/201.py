from collections import defaultdict


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], cap: int) -> int:
        graph = defaultdict(list)

        for i in edges:
            graph[i[0]].append([i[1], i[2]])
            graph[i[1]].append([i[0], i[2]])

        self.ans = -1
        self.mi = float('inf')

        def bfs(parent):
            seen = {parent: -1}
            q = [(parent, 0)]
            while(q != []):
                tem_node, used = q.pop(0)
                for node, dist in graph[tem_node]:
                    if((node not in seen or dist + used < seen[node]) and (dist + used) <= cap):
                        q.append((node, dist + used))
                        seen[node] = dist + used
            if(self.mi > len(seen)):
                self.mi = len(seen)
                self.ans = parent
            elif(self.mi == len(seen) and parent > self.ans):
                self.ans = parent

        for i in range(n):
            bfs(i)

        return self.ans
