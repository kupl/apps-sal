class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        index = 0
        count = 1
        counter = 0
        
        while True:
            
            
            if not count in arr:
                counter += 1
                if counter == k:
                    return count
            index += 1
            count += 1

