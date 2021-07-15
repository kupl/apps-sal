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
        
        cum = []
        prevSums = [0] * n
        for r in range(m):
            rowSum = 0
            cumSums = []
            for c in range(n):
                rowSum += mat[r][c]
                cumSums.append(prevSums[c] + rowSum)
            cum.append(cumSums)
            prevSums = cumSums
        
        out = []
        for i in range(m):
            blockSums = []
            for j in range(n):
                r = i + K if i + K < m else m - 1
                c = j + K if j + K < n else n - 1
                
                blockSum = cum[r][c]
                if i - K > 0:
                    blockSum -= cum[i-K-1][c]
                if j - K > 0:
                    blockSum -= cum[r][j-K-1]
                if i - K > 0 and j - K > 0:
                    blockSum += cum[i-K-1][j-K-1]
                blockSums.append(blockSum)
            out.append(blockSums)
        
        return out
