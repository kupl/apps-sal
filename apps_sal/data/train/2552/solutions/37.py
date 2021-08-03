class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return -1
        if len(arr) == 1:
            return arr[0]

        p1 = p2 = 0
        arrLen = len(arr)
        while p2 < arrLen:
            if arr[p2] != arr[p1]:
                if (p2 - p1) / arrLen > 0.25:
                    return arr[p1]
                p1 = p2
            p2 += 1
        return arr[p2 - 1]
