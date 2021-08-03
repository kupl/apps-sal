import heapq as pq


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])

        # Find first min, the 2nd min
        min_vals = []
        for i in range(cols):
            pq.heappush(min_vals, (arr[0][i], i))

        min_vals = pq.nsmallest(2, min_vals)

        for i in range(1, cols):
            # print(min_vals)

            new_min_vals = []
            (min_val2, _) = min_vals.pop()
            (min_val, min_col) = min_vals.pop()
            for col in range(cols):
                arr[i][col] += min_val if min_col != col else min_val2
                pq.heappush(new_min_vals, (arr[i][col], col))
            min_vals = pq.nsmallest(2, new_min_vals)
            # print(i, arr)
        return min(arr[-1])
