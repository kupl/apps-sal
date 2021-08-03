class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            firstMax, secMax = stones.pop(stones.index(max(stones))), stones.pop(stones.index(max(stones)))
            if firstMax - secMax != 0:
                stones.append(firstMax - secMax)
        if stones:
            return stones[0]
        else:
            return 0
