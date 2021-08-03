class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        result = []
        for x in prerequisites:
            graph[x[1]].append(x[0])
        print(graph)

        def dfs(i):
            if visit[i] == -1:
                return []
            if visit[i] == 1:
                return result
            visit[i] = -1
            for x in graph[i]:
                if [] == dfs(x):
                    return []
            visit[i] = 1
            result.append(i)
            return result

        for x in range(numCourses):
            if [] == dfs(x):
                return []
        return result[::-1]

        """
         :type numCourses: int
         :type prerequisites: List[List[int]]
         :rtype: List[int]
         """
