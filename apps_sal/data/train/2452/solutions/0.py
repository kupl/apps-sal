class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if y != x:
                stones.append(x-y)
            

