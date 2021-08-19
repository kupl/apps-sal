class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        count_balloon = 0
        count_b = 0
        count_a = 0
        count_l = 0
        count_o = 0
        count_n = 0
        for char in text:
            if char == 'b':
                count_b += 1
            elif char == 'a':
                count_a += 1
            elif char == 'l':
                count_l += 1
            elif char == 'o':
                count_o += 1
            elif char == 'n':
                count_n += 1
        count_balloon = min(count_b, count_a, count_l // 2, count_o // 2, count_n)
        return count_balloon
