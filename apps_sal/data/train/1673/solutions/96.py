import heapq, bisect
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr or not arr[0]:
            raise ValueError(\"empty input.\")
        
        m = len(arr) # row
        n = len(arr[0]) # col
        dp = [0] * n
        prev_min = [(0, -1), (0, -1)]

        for row in arr:
            dp_new = [0] * n
            curr_min = []
            for i, num in enumerate(row):
                if i == prev_min[0][1]:
                    dp_new[i] = prev_min[1][0] + num
                else:
                    dp_new[i] = prev_min[0][0] + num
                bisect.insort(curr_min, (dp_new[i], i))
                
                if len(curr_min) > 2:
                    curr_min.pop()
            prev_min = curr_min
            dp = dp_new
        return min(dp)
        # dp = [(x, i) for i, x in enumerate(arr[0])] # start with first row.
        # heapq.heapify(dp)
        # # O(mnlogn) solution
        # for row in arr[1:]:
        #     dp_new = []
        #     for i in range(n):
        #         if dp[0][1] == i:
        #             tmp = heapq.heappop(dp)
        #             heapq.heappush(dp_new, (dp[0][0] + row[i], i))
        #             heapq.heappush(dp, tmp)
        #         else:
        #             heapq.heappush(dp_new, (dp[0][0] + row[i], i))
        #     dp = dp_new
        # return dp[0][0]
#         # O(mn^2) solution:
#         for row in arr[1:]:
#             dp_new = [0] * n
#             for i in range(n):
#                 dp_new[i] = row[i] + min([x for i_prev, x in enumerate(dp) if i != i_prev])
#             dp = dp_new
            
#         return min(dp_new)
