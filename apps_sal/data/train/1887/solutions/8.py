class Solution(object):
    def findCircleNum(self, M):
        seen = set()

        def dfs(n):
            if n in seen:
                return
            # print('walk', n)
            seen.add(n)
            neighbors = [i for i, val in enumerate(M[n]) if val == 1]

            for neighbor in neighbors:
                dfs(neighbor)

        count = 0
        for j, row in enumerate(M):
            for i, item in enumerate(row):
                if j in seen or i in seen:
                    continue

                count += 1
                # print('start',j,i)
                dfs(i)

        return count
