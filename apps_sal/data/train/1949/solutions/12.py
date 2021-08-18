
'''class Solution:
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
        return res'''

'''def dfs(self, grid, x,y,rLen, cLen):
            val = grid[x][y]
            grid[x][y] = 0
            curSum = 0 
            path = []
            if x+1 < rLen and grid[x+1][y] != 0:
                ret, retPath = self.dfs(grid, x+1,y,rLen, cLen)
                if ret > curSum:
                    curSum = ret 
                    path = retPath
            if x-1 >=0 and grid[x-1][y] != 0:
                ret, retPath= self.dfs(grid, x-1,y,rLen, cLen)
                if ret > curSum:
                    curSum = ret
                    path = retPath
            if y+1 < cLen and grid[x][y+1] != 0:
                ret, retPath = self.dfs(grid, x,y+1,rLen, cLen)
                if ret > curSum:
                    curSum = ret
                    path = retPath
            if y-1 >= 0 and grid[x][y-1] != 0:
                ret, retPath = self.dfs(grid, x,y-1,rLen, cLen)
                if ret > curSum:
                    curSum = ret
                    path = retPath
            path.append([x,y])
            grid[x][y] = val
            return curSum + val, path'''


'''class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int: 
        self.rLen = len(grid)
        self.cLen = len(grid[0])
        res = 0 
        path = None 
        for i in range(self.rLen):
            for j in range(self.cLen):
                if grid[i][j] != 0:
                    ret, retPath = self.dfs(grid, i,j)
                    if ret > res:
                        res = ret 
                        path = retPath
        return res '''
'''
    def dfs(self, grid, i,j):
        if 0<=i<self.rLen and 0<=j<self.cLen and grid[i][j] != 0:
            tmp = grid[i][j]
            grid[i][j] = 0 
            total = 0 
            totalPath = []
            for newI, newJ in [[i+1,j], [i-1,j],[i,j+1],[i,j-1]]:
                count, path = self.dfs(grid,newI, newJ)
                if count + tmp > total:
                    total = count + tmp
                    totalPath = path + [[i,j]]
            grid[i][j] = tmp
            return total, totalPath
        else:
            return 0, []'''


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.rLen = len(grid)
        self.cLen = len(grid[0])
        res = 0
        path = None
        for i in range(self.rLen):
            for j in range(self.cLen):
                if grid[i][j] != 0:
                    ret, retPath = self.dfs(grid, i, j)
                    if ret > res:
                        res = ret
                        path = retPath
        return res
    '''def dfs(self, grid,i,j):
        if 0<=i<self.rLen and 0<=j<self.cLen and grid[i][j] != 0:
            tmp = grid[i][j]
            grid[i][j] = 0 
            maxTotal = 0 
            maxPath = []
            for newI, newJ in [[i+1, j],[i-1,j],[i,j+1],[i,j-1]]:
                retTotal, retPath = self.dfs(grid, newI, newJ)
                if retTotal + tmp > maxTotal:
                    maxTotal = retTotal + tmp 
                    maxPath = retPath 
            grid[i][j] = tmp 
            return maxTotal, maxPath 
        else:
            return 0, []'''

    def dfs(self, grid, i, j):
        if grid[i][j] != 0:
            tmp = grid[i][j]
            grid[i][j] = 0
            maxTotal = 0
            maxPath = []
            for newI, newJ in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= newI < len(grid) and 0 <= newJ < len(grid[0]) and grid[newI][newJ] != 0:
                    retTotal, retPath = self.dfs(grid, newI, newJ)
                    if retTotal > maxTotal:
                        maxTotal = retTotal
                        maxPath = retPath
            grid[i][j] = tmp
            return maxTotal + tmp, maxPath + [(i, j)]
        else:
            return 0, []


'''from collections import namedtuple
class Solution:
    neighbor = namedtuple('neighbor', ('idx', 'w'))
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(v, availa_lst, sum_, max_sum):
            sum_ += v.w
            if all([availa_lst[neibr.idx] for neibr in adj_list[v.idx]]):
                return [True, max(sum_, max_sum)]
            for neibr in adj_list[v.idx]:
                if not availa_lst[neibr.idx]:
                    availa_lst[neibr.idx] = True
                    res, sum_path = dfs(neibr, availa_lst, sum_, max_sum)
                    if res:
                        max_sum = max(max_sum, sum_path)
                    availa_lst[neibr.idx] = False
            return [True, max_sum]
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        V = [(row * m) + col for row in range(n) for col in range(m) if grid[row][col] != 0]
        dict_ = {V[x]: x for x in range(len(V))}
        adj_list = []
        for v in V:
            tmp_adj = []
            v_row, v_col = v//m, v%m
            if v_row != 0 and grid[v_row - 1][v_col] != 0:  
                up_idx = dict_[v-m]
                tmp_adj.append(self.neighbor(up_idx, grid[v_row-1][v_col]))
            if v_row != (n-1) and grid[v_row + 1][v_col] != 0:  
                dow_idx = dict_[v+m]
                tmp_adj.append(self.neighbor(dow_idx, grid[v_row+1][v_col]))
            if v_col != 0 and grid[v_row][v_col - 1] != 0:  
                left_idx = dict_[v-1]
                tmp_adj.append(self.neighbor(left_idx, grid[v_row][v_col-1]))
            if v_col != (m-1) and grid[v_row][v_col+1] != 0:  
                right_idx = dict_[v+1]
                tmp_adj.append(self.neighbor(right_idx, grid[v_row][v_col+1]))
            adj_list.append(tmp_adj)
        max_path = -float('inf')
        checked = [False] * len(V)
        for v_idx, v in enumerate(V):
            row, col = v//m, v%m
            checked[v_idx] = True
            max_path = max(max_path, dfs(self.neighbor(v_idx, grid[row][col]), checked, 0, -float('inf'))[1])
            checked[v_idx] = False
        return max_path'''


'''import functools
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(u, visited):                
            subres = 0
            for v in graph[u]:
                if (visited >> v) & 1 == 0: 
                    subres = max(subres, dfs(v, visited | (1 << v)))
            return vertex_gold[u] + subres  

        vertex_gold = [] 
        m = {}           
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:
                    m[i, j] = len(vertex_gold)  
                    vertex_gold.append(cell)    
        graph = collections.defaultdict(list)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell:                    
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y]:
                            graph[m[i, j]].append(m[x, y])
        return max(dfs(u, 1 << u) for u in range(len(vertex_gold))) '''
