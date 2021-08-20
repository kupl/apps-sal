class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        li = []
        sumv = 0
        n = len(arr)
        for i in range(1, n + 1, 2):
            li.append(i)
        for i in li:
            for j in range(len(arr)):
                if i + j <= n:
                    sumv += sum(arr[j:j + i])
                else:
                    break
        return sumv
