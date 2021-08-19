class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        #    last = len(arr)
        #    total = 0
     #   for start in range(len(arr)):
     #       end = start
     #       while end < last:
     #           total += sum(arr[start:end+1])
     #           end += 2   '''
     #       return total

        total = 0
        for i in range(len(arr)):
            totalisubarrays = (len(arr) - i) * (i + 1)  # this represent total number of subarrays in list that has either i as start or end.
            if totalisubarrays % 2 == 1:
                totalisubarrays += 1
            oddisubarrays = totalisubarrays // 2
            total += arr[i] * oddisubarrays
        return total
