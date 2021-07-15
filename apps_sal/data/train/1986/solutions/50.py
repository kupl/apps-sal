class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        r = [0, 1]
        for i in range(1, n):
            r += [2 ** i + v for v in r[::-1]]
        idx = r.index(start)
        return r[idx:] + r[:idx]
