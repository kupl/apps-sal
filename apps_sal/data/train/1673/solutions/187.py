class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        min_path = float(\"inf\")
        n = len(arr)
        m = len(arr[0])
        for r in range(1, n):
            min_path = float(\"inf\")
            for c in range(0, m):
                if (c == 0):
                    arr[r][c] += min(arr[r-1][1:])
                elif(c == m):
                    arr[r][c] += min(arr[r-1][:-1])
                else:
                    arr[r][c] += min(arr[r-1][:c]+arr[r-1][c+1:])
                min_path = min(min_path, arr[r][c])

        return min_path
                                
                                 
        
                                 
