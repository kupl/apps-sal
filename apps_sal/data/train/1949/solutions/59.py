class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # d表示四个方向，分别是左、上、右、下，二维查找问题一般都会用到这个
        d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        m = len(grid)
        if m == 0:  # 空grid=[]，那就直接退出0
            return 0
        n = len(grid[0])

        # 初始化 visited 全部为了False，为了标记 这个点是否已经走过
        visited = []
        visited_in = []
        for i in range(m):
            for j in range(n):
                visited_in.append(False)
            visited.append(visited_in)
            visited_in = []

        # 判断x和y是否再board这个表格里面
        def inArea(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        # Floorfill算法！每次遍历到一个点，那就找上下左右
        def DFS(grid, startx, starty):
            res = 0
            visited[startx][starty] = True  # 标记已经走过的点
            # 上下左右四个方向
            for i in range(4):
                newx = startx + d[i][0]  # 更新x
                newy = starty + d[i][1]  # 更新y
                # 新点必须满足以下三个条件，也就是再正常取值范围内m/n，没有被访问 并且这个新点的值不能为0，就会不断递归
                if inArea(newx, newy) and (not visited[newx][newy]) and grid[newx][newy] != 0:
                    # 每到一个点，就搜索旁边的四个点，并且相加，最后在与之前最大的res比较，要是res比较大，那就替代掉原来的res
                    res = max(res, grid[newx][newy] + DFS(grid, newx, newy))

            # 每次循环完上下左右四个点后，再把原先的点标记为没有浏览过，是为了后面 重复寻找！
            visited[startx][starty] = False
            return res

        record_each_result = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (not visited[i][j]):
                    result = grid[i][j] + DFS(grid, i, j)
                    record_each_result.append(result)

        # final result
        final_result = max(record_each_result)
        # print(final_result)
        return final_result
