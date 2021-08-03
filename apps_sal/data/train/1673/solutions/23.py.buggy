class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        min_path = float(\"inf\")
        n = len(arr)
        m = len(arr[0])
        for r in range(1, n):
            min_path = float(\"inf\")
            for c in range(0, m):
                arr[r][c] += sorted(arr[r-1][:c]+arr[r-1][c+1:])[0]
                min_path = min(min_path, arr[r][c])

        return min_path
                                
                                 
        
                                 
