class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arrayLength = len(arr) + 1
        oddLengthSum = 0
        
        if (arrayLength <= 2):
            return sum(arr)
        
        for subArrayLength in range(arrayLength)[1::2]:
            for i in range(arrayLength - subArrayLength):
                for value in arr[i:i + subArrayLength]:
                    oddLengthSum += value
        
        return oddLengthSum

