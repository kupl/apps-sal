class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []

        for i in range(2**n):
            res.append((i >> 1) ^ i)

        idx = res.index(start)
        return res[idx:] + res[:idx]
