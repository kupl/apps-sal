class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        xdict = {}
        print(arr[0:1])
        for i in range(0, len(arr)):
            sumx = 0
            for j in range(0, len(arr) - i):
                sumx = sumx + sum(arr[j:j + i + 1])
            xdict[i] = sumx

        print(xdict)
        sumx = 0
        for i in xdict:
            if i % 2 == 0:
                sumx = sumx + xdict[i]

        return sumx
