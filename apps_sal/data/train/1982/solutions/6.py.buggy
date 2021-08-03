
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

