# 886. Possible Bipartition

class Solution1:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        g = collections.defaultdict(list)
        for u, v in dislikes:
            g[u].append(v)
            g[v].append(u)
            
        color = {}
        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c^1) for nei in g[node])
        
        return all(dfs(node)
                   for node in range(1, N+1)
                   if node not in color)
    
    
\"\"\"
    1st approach: BFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    780 ms, faster than 28.52%
\"\"\"


class Solution2(object):
    def possibleBipartition(self, N, dislikes):
        \"\"\"
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        \"\"\"
        connections = []
        for _ in range(N+1):
            connections.append([])

        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)

        seen = {}
        for i in range(len(connections)):
            if i not in seen:
                if self.check(connections, i, seen) == False:
                    return False
        return True

    def check(self, connections, start, seen):
        q = [(start, 1)]
        while len(q) > 0:
            pop, color = q.pop(0)
            if pop in seen:
                if seen[pop] != color:
                    return False
                continue
            seen[pop] = color
            vertices = connections[pop]
            for v in vertices:
                q.append((v, -color))
        return True


\"\"\"
    2nd approach: recursive DFS + nodes coloring

    Time    O(V+E)
    Space   O(V+E)
    660 ms, faster than 53.79%
\"\"\"


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        \"\"\"
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        \"\"\"
        connections = []
        for _ in range(N+1):
            connections.append([])

        for a, b in dislikes:
            connections[a].append(b)
            connections[b].append(a)

        seen = {}
        for i in range(len(connections)):
            if i not in seen:
                if self.check(connections, i, 1, seen) == False:
                    return False
        return True

    def check(self, connections, node, color, seen):
        if node in seen:
            if seen[node] != color:
                return False
            return True
        seen[node] = color
        vertices = connections[node]
        for v in vertices:
            if self.check(connections, v, -color, seen) == False:
                return False
        return True
