class Solution:
    def binaryGap(self, n: int) -> int:
        maxDist = 0
        currDist = 0
        while n:
            if n & 1 and currDist != 0:
                maxDist = max(maxDist, currDist)
                currDist = 1
            elif n & 1:
                currDist = 1
            elif not n & 1 and currDist != 0:
                currDist += 1
            n >>= 1
        return maxDist
