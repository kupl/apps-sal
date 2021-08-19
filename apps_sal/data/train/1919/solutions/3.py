class Solution:

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        nums = [[] for _ in range(numCourses)]
        du = [0] * numCourses
        for (end, start) in prerequisites:
            nums[start].append(end)
            du[end] += 1
        result = []

        def dfs(idx):
            du[idx] -= 1
            result.append(idx)
            for i in nums[idx]:
                du[i] -= 1
                if du[i] == 0:
                    dfs(i)
        for i in range(numCourses):
            if du[i] == 0:
                dfs(i)
        if len(result) == numCourses:
            return result
        return []
