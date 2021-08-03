class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [0] * (1 << n)
        for i in range(1 << n):
            res[i] = start ^ i ^ i >> 1
        return res
