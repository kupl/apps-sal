class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        total = 0
        for num in target:
            if num > prev:
                total += num-prev
            prev = num
        return total
                
            
        
            

