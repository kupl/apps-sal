class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        counts = Counter(A)
        increments = 0
        for num in range(100000):
            count = counts[num]
            if count > 1:
                increments += count - 1
                counts[num] = 1
                if not counts[num + 1]:
                    counts[num + 1] = 0
                counts[num + 1] += count - 1
        return increments
