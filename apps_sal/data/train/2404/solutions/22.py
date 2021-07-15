class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        counter = set()
        for i in arr:
            counter.add(i)
        
        result = []
        
        position = 1
        while k > 0:
            if position not in counter:
                k -= 1 
            position += 1
            
        return position - 1
            
            

