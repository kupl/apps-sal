class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i = max(stones)
        weights = [0] * (i + 1)
        for stone in stones:
            weights[stone] += 1
        current = 0
        while i > 0:
            if weights[i] != 0:
                if current == 0:
                    current = i
                    weights[i] -= 1
                else:
                    current -= i
                    weights[i] -= 1
                    if current > i:
                        i = current
                    weights[current] += 1
                    current = 0
            else:
                i -= 1
        return current
