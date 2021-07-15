class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                a = arr[i:j + 1]
                
                if not len(a) % 2 == 0:
                    total += sum(a)
        return total
