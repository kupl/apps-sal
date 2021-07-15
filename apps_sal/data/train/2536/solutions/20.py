class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = [num for num in arr if arr.count(num) == num]
        return max(res) if res else -1
        
        
        

