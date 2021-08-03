class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def dfs(v, edgesOut, seen, pCounts):
            if seen[v] == 1:
                return []
            else:
                if pCounts[v] > 0:
                    return []
                else:
                    seen[v] = 1
                    order = [v]
                    for e in edgesOut[v]:
                        pCounts[e] -= 1
                    for e in edgesOut[v]:
                        order += dfs(e, edgesOut, seen, pCounts)
                    return order

        seen = [0] * numCourses
        pCounts = [0] * numCourses
        edgesOut = [[] for __ in range(numCourses)]
        edgesIn = [[] for __ in range(numCourses)]
        for (a, b) in prerequisites:
            edgesOut[b].append(a)
            edgesIn[a].append(b)
            pCounts[a] += 1

        order = []
        for v in range(numCourses):
            order += dfs(v, edgesOut, seen, pCounts)

        if len(order) < numCourses:
            return []
        else:
            return order
