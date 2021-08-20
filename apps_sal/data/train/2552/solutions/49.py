class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        start = True
        d = 0
        count = 0
        if len(arr) == 1:
            return arr[0]
        for v in arr:
            if start:
                start = False
                d = v
                count = 1
            elif v == d:
                count += 1
                if len(arr) % 4 == 0 and count > len(arr) / 4:
                    return v
                if len(arr) % 4 != 0 and count >= len(arr) // 4 + 1:
                    return v
            else:
                d = v
                count = 1
        return 0
