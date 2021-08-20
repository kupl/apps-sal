class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        m = len(arr)
        s = 0
        a = []
        for i in range(m):
            t = 0
            while t <= m:
                a = arr[i:t]
                t += 1
                if len(a) % 2 != 0:
                    s = s + sum(a)
        return s
