class Solution:

    def maxScore(self, s: str) -> int:
        count_0 = 0
        count_1 = 0
        result = []
        for i in range(0, len(s) - 1):
            if s[i] == '0':
                count_0 += 1
            for j in range(i + 1, len(s)):
                if s[j] == '1':
                    count_1 += 1
            result += [count_0 + count_1]
            count_1 = 0
        return max(result)
