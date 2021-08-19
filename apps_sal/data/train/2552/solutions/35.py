class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        limit = len(arr) // 4
        curr = arr[0]
        count = 1

        # print(len(arr), limit)

        for i in range(1, len(arr)):
            if arr[i] != curr:
                curr = arr[i]
                count = 1
                continue
            else:
                count += 1
                if count > limit:
                    return curr
