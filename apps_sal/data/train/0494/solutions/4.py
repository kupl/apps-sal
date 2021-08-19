class Solution:

    def longestDecomposition(self, text: str) -> int:
        found = {}

        def search(start, end):
            if start > end:
                return 0
            if (start, end) in found:
                return found[start, end]
            m = 1
            for i in range(1, (end - start + 1) // 2 + 1):
                if text[start:start + i] == text[end + 1 - i:end + 1]:
                    m = max(m, 2 + search(start + i, end - i))
            found[start, end] = m
            return m
        return search(0, len(text) - 1)
