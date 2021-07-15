class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if arr == []:
            return 0
        
        sum_ = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                val = arr[i : j]
                if len(val) % 2 != 0:
                    sum_ += sum(val)
        
        return sum_
