class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        m = len(mat)
        n = len(mat[0])
        data = [[0 for _ in range(n)] for _ in range(m)] # [i, j] stores consecutive number of 1s from the cell upwards
        for row in range(m): # row
            for col in range(n): # col
                if not mat[row][col]:
                    continue
                data[row][col] = 1 if row == 0 else data[row - 1][col] + 1
                smallest = data[row][col]
                res += smallest
                for j in range(col - 1, -1, -1):
                    smallest = min(smallest, data[row][j])
                    res += smallest
        return res

    
    def numSubmat_v1(self, mat: List[List[int]]) -> int:
        \"\"\"My O(n^4) algorithm
        \"\"\"
        res = 0
        m = len(mat)
        n = len(mat[0])
        data = [[set() for _ in range(n)] for _ in range(m)] # [i, j] stores valid rectangle sizes represented by longth & width
        for row in range(m): # row
            for col in range(n): # col
                if not mat[row][col]:
                    continue
                data[row][col].add((1,1))
                res += 1
                if col > 0:
                    for e in data[row][col - 1]:  # look at all rectangles of the left cell
                        if e[1] == 1:
                            data[row][col].add((e[0] + 1, 1))
                            res += 1
                        elif row > 0 and (1, e[1] - 1) in data[row - 1][col]:
                            data[row][col].add((e[0] + 1, e[1]))
                            res += 1
                if row > 0:
                    for e in data[row - 1][col]:
                        if e[0] == 1:
                            data[row][col].add((1, e[1] + 1))
                            res += 1
        return res
                
                
