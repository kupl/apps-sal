class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        splits = 0
        leftstart, leftend = 0, 0
        rightstart, rightend = n - 1, n - 1
        while leftend < rightstart:
            if text[leftstart:leftend + 1] == text[rightstart:rightend + 1]:
                leftstart = leftend + 1
                leftend = leftstart
                rightstart = rightstart - 1
                rightend = rightstart
                splits += 2
            else:
                leftend += 1
                rightstart -= 1
        return splits + 1 if leftstart <= rightend else splits
