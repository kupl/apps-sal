# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         result = 0

#         for i, num in enumerate(arr):
#             for j, num in enumerate(arr):
#                 for k, num in enumerate(arr):
#                     if i < j < k and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                         result += 1
#         return result


from itertools import combinations


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        C = list(combinations(arr, 3))
        C = [self.checkGood(x, a, b, c) for x in C]
        C = [x for x in C if x != None]
        # print(C)
        return len(C)

    def checkGood(self, tup, a, b, c):
        if abs(tup[0] - tup[1]) <= a and abs(tup[0] - tup[2]) <= c and abs(tup[2] - tup[1]) <= b:
            return tup
