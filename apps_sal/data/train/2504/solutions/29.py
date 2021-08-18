class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return (arr[0])
        result = 0
        l = r = 0

        def getSum(array, start, end):
            local_sum = 0
            for i in range(start, end):
                local_sum += array[i]
            return local_sum

        while l < len(arr) - 1:
            if r > len(arr) - 1:
                l += 1
                r = l
            result += getSum(arr, l, r + 1)
            r += 2
        return result
