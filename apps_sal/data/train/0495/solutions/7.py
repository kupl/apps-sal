class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:

        cache = {}

        def diffs(s1: int, s2: int, xs: List[int]) -> int:
            if len(xs) == 0:
                return abs(s1 - s2)

            if (s1, s2, len(xs)) not in cache:
                y = xs.pop()
                min_val = min(diffs(s1 + y, s2, xs), diffs(s1, s2 + y, xs))
                xs.append(y)
                cache[(s1, s2, len(xs))] = min_val

            return cache[(s1, s2, len(xs))]

        return diffs(stones[0], 0, stones[1:])
