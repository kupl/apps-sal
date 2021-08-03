class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        used = []
        ans = 0
        for x in range(41000):
            if count[x] >= 2:
                used.extend([x] * (count[x] - 1))
            elif used and count[x] == 0:
                ans += x - used.pop()
        return ans

#         count = collections.Counter(A)
#         taken = []

#         ans = 0
#         for x in range(100000):
#             if count[x] >= 2:
#                 taken.extend([x] * (count[x] - 1))
#             elif taken and count[x] == 0:
#                 ans += x - taken.pop()
#         return ans
