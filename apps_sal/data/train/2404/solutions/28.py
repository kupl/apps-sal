class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        x = 1
    
        count = 0
        while count !=k:
            if x not in arr:
                count = count+1
                if count ==k:
                    return x
            x = x+1
                

