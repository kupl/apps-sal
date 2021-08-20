"""class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:       
        rLen = len(grid)
        if rLen == 0:
            return 0 
        cLen = len(grid[0])
        if cLen == 0:
            return 0 
        res = 0 
        resPath = []
        for i in range(rLen):
            for j in range(cLen):
                if grid[i][j] != 0 and [i,j] not in resPath:
                    tmp, path = self.dfs(grid, i,j,rLen, cLen)
                    if tmp > res:
                        res = tmp
                        resPath = path
        return res"""
'def dfs(self, grid, x,y,rLen, cLen):\n            val = grid[x][y]\n            grid[x][y] = 0\n            curSum = 0 \n            path = []\n            if x+1 < rLen and grid[x+1][y] != 0:\n                ret, retPath = self.dfs(grid, x+1,y,rLen, cLen)\n                if ret > curSum:\n                    curSum = ret \n                    path = retPath\n            if x-1 >=0 and grid[x-1][y] != 0:\n                ret, retPath= self.dfs(grid, x-1,y,rLen, cLen)\n                if ret > curSum:\n                    curSum = ret\n                    path = retPath\n            if y+1 < cLen and grid[x][y+1] != 0:\n                ret, retPath = self.dfs(grid, x,y+1,rLen, cLen)\n                if ret > curSum:\n                    curSum = ret\n                    path = retPath\n            if y-1 >= 0 and grid[x][y-1] != 0:\n                ret, retPath = self.dfs(grid, x,y-1,rLen, cLen)\n                if ret > curSum:\n                    curSum = ret\n                    path = retPath\n            path.append([x,y])\n            grid[x][y] = val\n            return curSum + val, path'
'class Solution:\n    def getMaximumGold(self, grid: List[List[int]]) -> int: \n        self.rLen = len(grid)\n        self.cLen = len(grid[0])\n        res = 0 \n        path = None \n        for i in range(self.rLen):\n            for j in range(self.cLen):\n                if grid[i][j] != 0:\n                    ret, retPath = self.dfs(grid, i,j)\n                    #print(grid)\n                    if ret > res:\n                        res = ret \n                        path = retPath\n        return res '
'\n    def dfs(self, grid, i,j):\n        if 0<=i<self.rLen and 0<=j<self.cLen and grid[i][j] != 0:\n            tmp = grid[i][j]\n            grid[i][j] = 0 \n            total = 0 \n            totalPath = []\n            for newI, newJ in [[i+1,j], [i-1,j],[i,j+1],[i,j-1]]:\n                count, path = self.dfs(grid,newI, newJ)\n                if count + tmp > total:\n                    total = count + tmp\n                    totalPath = path + [[i,j]]\n            grid[i][j] = tmp\n            return total, totalPath\n        else:\n            return 0, []'


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.rLen = len(grid)
        self.cLen = len(grid[0])
        res = 0
        path = None
        for i in range(self.rLen):
            for j in range(self.cLen):
                if grid[i][j] != 0:
                    (ret, retPath) = self.dfs(grid, i, j)
                    if ret > res:
                        res = ret
                        path = retPath
        return res
    'def dfs(self, grid,i,j):\n        if 0<=i<self.rLen and 0<=j<self.cLen and grid[i][j] != 0:\n            tmp = grid[i][j]\n            grid[i][j] = 0 \n            maxTotal = 0 \n            maxPath = []\n            for newI, newJ in [[i+1, j],[i-1,j],[i,j+1],[i,j-1]]:\n                retTotal, retPath = self.dfs(grid, newI, newJ)\n                if retTotal + tmp > maxTotal:\n                    maxTotal = retTotal + tmp \n                    maxPath = retPath \n            grid[i][j] = tmp \n            return maxTotal, maxPath \n        else:\n            return 0, []'

    def dfs(self, grid, i, j):
        if grid[i][j] != 0:
            tmp = grid[i][j]
            grid[i][j] = 0
            maxTotal = 0
            maxPath = []
            for (newI, newJ) in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= newI < len(grid) and 0 <= newJ < len(grid[0]) and (grid[newI][newJ] != 0):
                    (retTotal, retPath) = self.dfs(grid, newI, newJ)
                    if retTotal > maxTotal:
                        maxTotal = retTotal
                        maxPath = retPath
            grid[i][j] = tmp
            return (maxTotal + tmp, maxPath + [(i, j)])
        else:
            return (0, [])


"from collections import namedtuple\nclass Solution:\n    neighbor = namedtuple('neighbor', ('idx', 'w'))\n    def getMaximumGold(self, grid: List[List[int]]) -> int:\n        def dfs(v, availa_lst, sum_, max_sum):\n            sum_ += v.w\n            if all([availa_lst[neibr.idx] for neibr in adj_list[v.idx]]):\n                return [True, max(sum_, max_sum)]\n            for neibr in adj_list[v.idx]:\n                if not availa_lst[neibr.idx]:\n                    availa_lst[neibr.idx] = True\n                    res, sum_path = dfs(neibr, availa_lst, sum_, max_sum)\n                    if res:\n                        max_sum = max(max_sum, sum_path)\n                    availa_lst[neibr.idx] = False\n            return [True, max_sum]\n        if not grid:\n            return 0\n        n, m = len(grid), len(grid[0])\n        # create vertices\n        V = [(row * m) + col for row in range(n) for col in range(m) if grid[row][col] != 0]\n        # create adjacency list\n        dict_ = {V[x]: x for x in range(len(V))}\n        adj_list = []\n        for v in V:\n            tmp_adj = []\n            v_row, v_col = v//m, v%m\n            if v_row != 0 and grid[v_row - 1][v_col] != 0:  # upper neighbor\n                up_idx = dict_[v-m]\n                tmp_adj.append(self.neighbor(up_idx, grid[v_row-1][v_col]))\n            if v_row != (n-1) and grid[v_row + 1][v_col] != 0:  # lower neighbor\n                dow_idx = dict_[v+m]\n                tmp_adj.append(self.neighbor(dow_idx, grid[v_row+1][v_col]))\n            if v_col != 0 and grid[v_row][v_col - 1] != 0:  # left neighbor\n                left_idx = dict_[v-1]\n                tmp_adj.append(self.neighbor(left_idx, grid[v_row][v_col-1]))\n            if v_col != (m-1) and grid[v_row][v_col+1] != 0:  # right neighbor\n                right_idx = dict_[v+1]\n                tmp_adj.append(self.neighbor(right_idx, grid[v_row][v_col+1]))\n            adj_list.append(tmp_adj)\n        # DFS on all vertices\n        max_path = -float('inf')\n        checked = [False] * len(V)\n        for v_idx, v in enumerate(V):\n            row, col = v//m, v%m\n            checked[v_idx] = True\n            max_path = max(max_path, dfs(self.neighbor(v_idx, grid[row][col]), checked, 0, -float('inf'))[1])\n            checked[v_idx] = False\n        return max_path"
'import functools\nclass Solution:\n    def getMaximumGold(self, grid: List[List[int]]) -> int:\n        @functools.lru_cache(None)\n        def dfs(u, visited):                # memoize on current_vertex, path\n            subres = 0\n            for v in graph[u]:\n                if (visited >> v) & 1 == 0: # if neighbor is not in path then recurse\n                    subres = max(subres, dfs(v, visited | (1 << v)))\n            return vertex_gold[u] + subres  # return gold here plus the best sub-result\n\n        vertex_gold = [] # vertex_gold[vertex_id] stores amount of gold\n        m = {}           # map of grid coordinate to vertex id\n        for i, row in enumerate(grid):\n            for j, cell in enumerate(row):\n                if cell:\n                    m[i, j] = len(vertex_gold)  # populate map\n                    vertex_gold.append(cell)    # save gold\n        graph = collections.defaultdict(list)\n        for i, row in enumerate(grid):\n            for j, cell in enumerate(row):\n                if cell:                    # if gold, connect vertex to neighbors\n                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):\n                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:\n                            graph[m[i, j]].append(m[x, y])\n        return max(dfs(u, 1 << u) for u in range(len(vertex_gold))) '
