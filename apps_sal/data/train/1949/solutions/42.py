import collections


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # collect the that I can start of with!!
        m = 0
        start = []
        cl, rl = len(grid[0]), len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    start.append((i, j))
                    if m < grid[i][j]:
                        m = grid[i][j]
        ans = []

        # print(start)
        for i in start:
            r, c = i
            s = str(r) + str(c)
            q = collections.deque()
            q.append([r, c, grid[r][c], s])

            while(q):
                l = q.popleft()
                r, c, s, path = l[0], l[1], l[2], l[3]

                # Flag initialization:
                lf = rf = uf = df = False

                # left
                if c - 1 >= 0 and grid[r][c - 1]:
                    k = str(r) + str(c - 1)
                    if k not in path:
                        v = grid[r][c - 1]
                        q.append([r, c - 1, s + v, path + '->' + k])
                        lf = True

                # right
                if c + 1 < cl and grid[r][c + 1]:
                    k = str(r) + str(c + 1)
                    if k not in path:
                        v = grid[r][c + 1]
                        q.append([r, c + 1, s + v, path + '->' + k])
                        rf = True

                # up
                if r - 1 >= 0 and grid[r - 1][c]:
                    k = str(r - 1) + str(c)
                    if k not in path:
                        v = grid[r - 1][c]
                        q.append([r - 1, c, s + v, path + '->' + k])
                        uf = True

                # down
                if r + 1 < rl and grid[r + 1][c]:
                    k = str(r + 1) + str(c)
                    if k not in path:
                        v = grid[r + 1][c]
                        q.append([r + 1, c, s + v, path + '->' + k])
                        df = True
                if not df and not uf and not lf and not rf:
                    ans.append(s)
        return max(ans)
