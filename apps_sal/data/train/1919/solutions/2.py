class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for i in range(0, numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        mark = [0] * numCourses
        order = []
        for i in range(0, numCourses):
            if mark[i] == 0:
                if not self.DFS(graph, i, mark, order):
                    return []

        res = []
        for i in range(len(order) - 1, -1, -1):
            res.append(order[i])

        return res

    def DFS(self, graph, index, mark, order):
        mark[index] = 1
        for vertex in graph[index]:
            if mark[vertex] == 0:
                if not self.DFS(graph, vertex, mark, order):
                    return False
            elif mark[vertex] == 1:
                return False

        mark[index] = 2
        order.append(index)
        return True
