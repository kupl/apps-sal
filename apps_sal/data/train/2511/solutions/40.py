class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        rep = {}
        for item in A:
            if item not in rep:
                rep[item] = 1
            else:
                return item
        return None
