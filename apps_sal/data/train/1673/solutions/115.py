class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n):
            lowest = min(arr[i - 1])
            lowestCount = 0
            secondLowest = float('inf')
            for j in range(len(arr[0])):
                if arr[i - 1][j] == lowest:
                    lowestCount += 1
                    
                if arr[i - 1][j] > lowest:
                    secondLowest = min(secondLowest, arr[i - 1][j])
                    
            if lowestCount >= 2:
                secondLowest = lowest
            
            for j in range(len(arr[0])):
                if arr[i-1][j] == lowest:
                    arr[i][j] += secondLowest
                else:
                    arr[i][j] += lowest
                
        return min(arr[n - 1])
                        
                    

