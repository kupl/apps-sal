class Solution:
    def sumHelper(self, mat: List[List[int]], rowLow: int, rowHigh: int, colLow: int, colHigh: int) -> int:
        res = 0
        for r in range(rowLow, rowHigh + 1):
            for c in range(colLow, colHigh + 1):
                res += mat[r][c]
        return res
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        res = [[0 for c in range(cols)] for r in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                lowR = r - K
                if (lowR < 0): lowR = 0
                highR = r + K
                if (highR >= rows): highR = rows - 1
                    
                lowC = c - K
                if (lowC < 0): lowC = 0
                highC = c + K
                if (highC >= cols): highC = cols - 1
        
                res[r][c] = self.sumHelper(mat, lowR, highR, lowC, highC)
        
        return res
