class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return (arr[0])
        result = 0
        l = r = 0

        def getSum(array, start, end):
            local_sum = 0
            for i in range(start, end):
                local_sum += array[i]  # 1,
            return local_sum

        while l < len(arr) - 1:  # 0<4
            if r > len(arr) - 1:  # 1>4
                l += 1
                r = l
            result += getSum(arr, l, r + 1)  # arr,0,2
            r += 2
        return result
