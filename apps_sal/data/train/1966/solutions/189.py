class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat);
        cols = len(mat[0]);
        dp = [[0 for _ in range(cols)] for _ in range(rows)];
        for r in range(rows):
            for c in range(cols):
                if c == 0:
                    dp[r][c] = mat[r][c];
                else:
                    if mat[r][c] == 1:
                        dp[r][c] = dp[r][c-1] + 1;
        count = 0;
        for r in range(rows):
            for c in range(cols):
                min_width = dp[r][c];
                for h_idx in range(r, -1, -1):
                    min_width = min(min_width, dp[h_idx][c]);
                    count += min_width
                    if min_width == 0:
                        break
        return count
