class Solution:
    def countLargestGroup(self, n: int) -> int:
        def numsum(x): return sum(map(int, list(str(x))))
        numdict = {}
        maxcount = 0

        for i in range(1, n + 1):
            x = numsum(i)
            numdict[x] = numdict.get(x, 0) + 1
            maxcount = max(maxcount, numdict[x])

        count = 0
        for i in numdict:
            if numdict[i] == maxcount:
                count += 1

        return count
