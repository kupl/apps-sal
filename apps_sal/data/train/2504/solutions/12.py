class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ret = 0
        for i in range(len(arr)):
            ret += arr[i] * ceil((len(arr) - i) * (i + 1) / 2)
        return ret

    # 1: 3
    # 4: 3
    # 2: 5
    # 5: 3
#     # 3: 3

#     (5-0)//2 -> 2
#     0//2-> 0
#     (5-1)//2 -> 2
#     1//2 -> 0
#     (5-2)//2 -> 1
#     2//2 -> 1
