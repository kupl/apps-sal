class Solution:
    def scan(self, row: List[int], n: int) -> (int, int, int):
        best = None
        k = None
        alt = None
        for j in range(n):
            if not best or row[j] < best:
                alt = best
                best = row[j]
                k = j
            elif not alt or row[j] < alt:
                alt = row[j]
        return best, k, alt
    
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        M = [[None for j in range(n)] for i in range(n)]

        for j in range(n):
            M[0][j] = arr[0][j]
        best, k, alt = self.scan(M[0], n)

        for i in range(1, n):
            for j in range(n):
                if j != k:
                    M[i][j] = arr[i][j] + best
                else:
                    M[i][j] = arr[i][j] + alt
            best, k, alt = self.scan(M[i], n)
        
        return best
