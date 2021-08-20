class Solution:

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        subArrLen = 1
        while subArrLen <= len(arr):
            i = 0
            j = subArrLen
            subTotal = sum(arr[:j])
            total += subTotal
            while j < len(arr):
                subTotal -= arr[i]
                subTotal += arr[j]
                total += subTotal
                i += 1
                j += 1
            subArrLen += 2
        return total
