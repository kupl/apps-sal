class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        d = [[float('-inf') for _ in range(n)] for _ in range(n)]
        for y in range(n):
            d[0][y] = arr[0][y]

        for x in range(1, n):
            smallest_two = heapq.nsmallest(2, d[x - 1])
            for y in range(n):
                if d[x - 1][y] == smallest_two[0]:
                    d[x][y] = smallest_two[1] + arr[x][y]
                else:
                    d[x][y] = smallest_two[0] + arr[x][y]

        ans = float('inf')
        for y in range(n):
            ans = min(ans, d[n - 1][y])
        return ans
