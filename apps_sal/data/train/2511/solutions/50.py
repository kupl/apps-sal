class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        occurences = set()
        for val in A:
            if val in occurences:
                return val
            occurences.add(val)
