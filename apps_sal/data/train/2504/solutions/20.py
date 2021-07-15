class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        s+=sum(arr)
    
        for j in range(3, len(arr)+1, 2):
            for i in range(0, len(arr)):
                if(len(arr[i:i+j])%2 != 0 and len(arr[i:i+j]) != 1 and                     i+j<=len(arr)):
                    s+=sum(arr[i:i+j])
        return s
