class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if numCourses <= 1:
            return [0]
        if not prerequisites:
            return [i for i in range(numCourses)]
        graph = [[] for _ in range(numCourses)]
        for pair in prerequisites:
            (x, y) = pair
            graph[x].append(y)
        (visited, visiting, topo) = (set(), set(), [])
        for i in range(numCourses):
            if i not in visited:
                if not self.topoOrder(graph, i, visited, visiting, topo):
                    return []
        return topo

    def topoOrder(self, graph, start, visited, visiting, topo):
        visited.add(start)
        visiting.add(start)
        adj_verts = graph[start]
        for vert in adj_verts:
            if vert in visiting:
                return False
            elif vert not in visited:
                if not self.topoOrder(graph, vert, visited, visiting, topo):
                    return False
        if start in visiting:
            visiting.remove(start)
        topo.append(start)
        return True
