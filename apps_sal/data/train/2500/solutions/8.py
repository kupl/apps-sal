class Solution:

    def maxPower(self, s: str) -> int:
        prev = None
        count = 0
        max_count = 0
        for char in s:
            if char == prev:
                count += 1
            else:
                prev = char
                count = 1
            max_count = max(max_count, count)
        return max_count
