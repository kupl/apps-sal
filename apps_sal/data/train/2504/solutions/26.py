class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for length in range(1, len(arr)+1):
            if length%2 == 0:
                continue
            for i_start, start in enumerate(arr):
                if i_start + length -1 < len(arr):
                    for i in range(i_start, i_start+length):
                        total += arr[i]
                else:
                    break
        return total
