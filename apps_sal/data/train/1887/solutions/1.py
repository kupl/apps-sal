class Solution:

    def dfs(self, M, cur):
        for i in range(len(M)):
            if flag[i]:
                continue
            if M[cur][i]:
                flag[i] = True
                self.dfs(M, i)

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        nonlocal flag
        flag = [False] * len(M)
        circle = 0

        for i in range(len(M)):
            if flag[i]:
                continue
            flag[i] = True
            circle += 1
            self.dfs(M, i)
        return circle
