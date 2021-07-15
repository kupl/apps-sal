
# class Solution {
#     public int twoCitySchedCost(int[][] costs) {
#         int N = costs.length / 2;
#         int[][] dp = new int[N + 1][N + 1];
#         for (int i = 1; i <= N; i++) {
#             dp[i][0] = dp[i - 1][0] + costs[i - 1][0];
#         }
#         for (int j = 1; j <= N; j++) {
#             dp[0][j] = dp[0][j - 1] + costs[j - 1][1];
#         }
#         for (int i = 1; i <= N; i++) {
#             for (int j = 1; j <= N; j++) {
#                 dp[i][j] = Math.min(dp[i - 1][j] + costs[i + j - 1][0], dp[i][j - 1] + costs[i + j - 1][1]);
#             }
#         }
#         return dp[N][N];
#     }
# }


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs) //2
        dp = [[0]*(N+1) for _ in range(N+1)]
        for i in range(1, N+1):
            dp[i][0] = dp[i-1][0] + costs[i-1][0]
        for j in range(1, N+1):
            dp[0][j] = dp[0][j-1] + costs[j-1][1]
        for i in range(1, N+1):
            for j in range(1, N+1):
                dp[i][j] = min(dp[i-1][j] + costs[i+j-1][0],
                              dp[i][j-1] + costs[i+j-1][1])
        for row in dp:
            print(row)
        return dp[N][N]

