class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    res -= 1
                    break
        return res

#         res = 0
#         cnt = 0
#         l = len(arr2)
#         for i in arr1:
#             for j in arr2:
#                 if abs(i - j) > d:
#                     cnt += 1
#             if cnt == l:
#                 res += 1
#                 cnt = 0
#         return res
