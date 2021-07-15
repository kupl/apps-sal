class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        N = 1 << n
        grey = [ i ^ (i >> 1) for i in range(N)]
        idx = grey.index(start)
        return grey[idx:] + grey[:idx]
