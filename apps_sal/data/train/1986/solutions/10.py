class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        a = ['0', '1']
        for i in range(n - 1):
            a0 = ['0' + b for b in a]
            a1 = ['1' + b for b in a]
            a = a0 + a1[::-1]
        intperm = [int(b, 2) for b in a]
        idx = intperm.index(start)
        return intperm[idx:] + intperm[:idx]
