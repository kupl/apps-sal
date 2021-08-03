class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        d = {}

        for value in A:
            if value in d:
                return value
            d[value] = 1
