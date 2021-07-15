class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        results = 0
        prev = None
        for num in A:
            if prev != None and num <= prev:
                results += (prev + 1) - num
                prev = prev + 1
            else:
                prev = num
        return results
