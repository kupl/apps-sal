class Solution:

    def longestDecomposition(self, text: str) -> int:
        count = 0
        i = 0
        while text:
            if text[:i + 1] == text[-(i + 1):]:
                count += 1
                if i + 1 < len(text):
                    count += 1
                text = text[i + 1:-(i + 1)]
                i = 0
                continue
            i += 1
        return count
