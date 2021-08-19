class Solution:

    def tribonacci(self, n: int) -> int:
        trib = []
        trib.append(0)
        trib.append(1)
        trib.append(1)
        for i in range(3, n):
            trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])
        if n > 2:
            return trib[n - 1] + trib[n - 2] + trib[n - 3]
        else:
            return trib[n]
