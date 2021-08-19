class Solution:

    def longestDecomposition(self, text: str) -> int:
        idxMap = defaultdict(list)
        for (i, ch) in enumerate(text):
            idxMap[ch].append(i)
        memo = {}

        def recurse(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            curMax = 1
            for k in idxMap[text[i]]:
                if k > j or i == k:
                    continue
                if text[i:i + j - k + 1] == text[k:j + 1]:
                    curMax = max(2 + recurse(i + j - k + 1, k - 1), curMax)
            memo[i, j] = curMax
            return curMax
        return recurse(0, len(text) - 1)
