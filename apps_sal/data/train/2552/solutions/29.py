class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[-1]
        k = int(len(arr) // 4) + 1
        c = 1
        for i in range(1, len(arr)):
            if arr[i - 1] == arr[i]:
                c += 1
                if c >= k:
                    return arr[i]
            else:
                c = 1
