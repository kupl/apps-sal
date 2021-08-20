class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        s = 0
        for i in range(l):
            for j in range(i + 1, l + 1, 2):
                subarr = arr[i:j]
                s += sum(subarr)
        return s
