class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        
        
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                
                curr_min = float(\"inf\")
                #need a for loop to try all directions.
                for k in range(len(arr[0])):                    
                    if k == j:
                        continue
                                        
                    if arr[i - 1][k] < curr_min:
                        curr_min = arr[i - 1][k]
                
                arr[i][j] += curr_min
                
                
        return min(arr[-1])

    
