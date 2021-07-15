from heapq import heappop, heappush, heapify 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
            
        # min heapify
        heapify(stones)
        while(len(stones) > 1):
            # get the max
            max1 = heappop(stones)
            max2 = heappop(stones)
            if -max1 - (-max2) > 0:
                heappush(stones, -(-max1 - (-max2)))
            # remove the max
            # get the max2
            # remove the max2
            
            
                # add -(-max1 - (-max2)) to the stones
        
        if len(stones) == 1:
            return -stones[0]
        return 0

