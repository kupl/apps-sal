class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            temp = 0
            for j in range(i, len(arr)):
                temp += arr[j]
                if (j - i) % 2 == 0:
                    total += temp
        return total
