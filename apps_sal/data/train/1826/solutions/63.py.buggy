class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        \"\"\"
        Brute force solution is to perform the sum for each position
        (r, c). This would require K * K operations for each of m * n positions.
        
        Instead, assuming we compute sums left to right and top down, we can
        use our previous solution to calculate the next one, subtracting the
        sums that fell out of the window and adding the sums that are in.
        
        Pseudo code would be something like this:
        
        prevBlockSum = ...
        for r in range(m):
            for c in range(n):
                if c - K > 0:
                    prevBlockSum -= sum()
        \"\"\"
        m = len(mat)
        n = len(mat[0])
        
        out = []
        for r in range(m):
            new_row = []
            for c in range(n):
                blockSum = 0
                
                rs = r-K if r-K >= 0 else 0
                re = r+K if r+K < m else m-1
                cs = c-K if c-K >= 0 else 0
                ce = c+K if c+K < n else n-1
                
                for i in range(rs, re+1):
                    for j in range(cs, ce+1):
                        blockSum += mat[i][j]
                
                new_row.append(blockSum)
            out.append(new_row)
        return out
