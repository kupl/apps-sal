class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        @lru_cache(None)
        def dfs(i, j):
            if i > j: return 0
            if i == j: return 1
            res = 1
            k = 1
            while i + k <= j - k + 1:
                if text[i:i+k] == text[j-k+1:j+1]:
                    res = max(res, 2 + dfs(i + k, j - k))
                k += 1
            return res
        return max(dfs(0, n - 1), 1)

