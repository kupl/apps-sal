class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for arr in grid:
            count += len(arr)-self.NegStart(arr)
        return count
        
    def NegStart(self, arr):
        first = 0
        last = len(arr)-1
        found = False
        while first<=last:
            midpoint = (first + last)//2
            if arr[midpoint] < 0:
                last = midpoint-1
            else:
                first = midpoint+1
        return first
            

