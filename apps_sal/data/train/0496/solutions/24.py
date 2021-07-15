class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        # [1, 2, 2, 2, 4, 4, 5]
        #     ^
        # [1, 2, 2, 2, 4, 4, 5]
        #        ^
        # [1, 2, 3, 4, 5, 6, 7] = 8
        
        count = collections.Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            # print(taken)
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans
