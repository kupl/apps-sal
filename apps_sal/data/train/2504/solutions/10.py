class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        for i in range(len(arr)):
            for j in range(len(arr) - i):
                start = j
                end = j + i + 1
                sub_arr = arr[start:end]
                if (end - start) % 2 == 1:
                    total_sum += sum(sub_arr)
        return total_sum
