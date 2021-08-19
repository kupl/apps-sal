class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        graph = {}
        for (post, pre) in prerequisites:
            if pre in graph:
                graph[pre].append(post)
            else:
                graph[pre] = [post]
        WHITE = 0
        GREY = 1
        BLACK = 2
        state = [WHITE for _ in range(0, n)]
        res = []

        def dfs(i):
            state[i] = GREY
            for child in graph.get(i, []):
                if state[child] == GREY:
                    return False
                elif state[child] == WHITE:
                    if not dfs(child):
                        return False
            state[i] = BLACK
            res.insert(0, i)
            return True
        for i in range(0, n):
            if state[i] != BLACK:
                if not dfs(i):
                    return []
        return res
