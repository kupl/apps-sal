class Solution:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0
        i, j, result = 0, len(text) - 1, 0
        while i < j:
            if text[:i + 1] == text[j:]:
                return self.longestDecomposition(text[i + 1: j]) + 2
            else:
                i, j = i + 1, j - 1
        return 1
