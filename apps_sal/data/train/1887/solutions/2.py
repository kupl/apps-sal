class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        ans = 0
        visited = [False for i in range(len(M))]

        def dfs(M, i, visited):
            visited[i] = True
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == False:
                    dfs(M, j, visited)

        for i in range(len(M)):
            if not visited[i]:
                dfs(M, i, visited)
                ans += 1
        return ans
