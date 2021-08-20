class Solution:

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        table = [i for i in range(n)]

        def find(x):
            tmp = x
            while table[tmp] != tmp:
                tmp = table[tmp]
            table[x] = tmp
            return tmp

        def union(x, y):
            table[find(x)] = find(y)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    union(i, j)
        print(table)
        return len(set((find(x) for x in range(n))))
