class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        arr = sorted(arr)[::-1]
        
        for i in arr:
            if(arr.count(i) == i):
                return i
        
        return -1
