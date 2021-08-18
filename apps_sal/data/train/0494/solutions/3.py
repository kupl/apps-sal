class Solution:
    def longestDecomposition(self, text: str) -> int:

        n = len(text)

        @lru_cache(None)
        def dp(left, right):

            if left > right:
                return 0

            if left == right:
                return 1

            maxk = 1
            length = 1
            while(left + length <= right - length + 1):
                if text[left:left + length] == text[right - length + 1:right + 1]:
                    maxk = max(maxk, dp(left + length, right - length) + 2)

                length += 1

            return maxk

        x = dp(0, n - 1)
        return x
