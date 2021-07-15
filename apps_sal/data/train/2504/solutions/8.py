class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        sum_arr = [[0] * (len(arr) + 1) for i in range (len(arr))]
        for i in range (len(arr)):
            for j in range (len(arr) - i):
                start = j
                end = j + i + 1
                sub_sum = 0
                if (end - start) == 1:
                    sum_arr[start][end] = arr[start]
                    sub_sum = arr[start]
                else:
                    sub_sum = arr[start] + sum_arr[start + 1][end]
                    sum_arr[start][end] = sub_sum
                if ((end - start) % 2 == 1):
                    total_sum += sub_sum
        return total_sum

