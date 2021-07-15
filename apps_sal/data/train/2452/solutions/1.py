class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ls = len(stones)
        if ls == 1:
            return stones[0]
        elif ls == 0:
            return 0
        stones.sort(reverse=True)
        while len(stones) > 1:
            stone1 = stones.pop(0)
            stone2 = stones.pop(0)
            if not stone1 == stone2:
                stone1 -= stone2
                stones.insert(0, stone1)
                stones.sort(reverse=True)
        try:
            return stones[0]
        except IndexError:
            return 0
