class Solution:

    def maxScore(self, s: str) -> int:
        list_score = []
        for i in range(1, len(s)):
            score = 0
            for j in s[:i]:
                if j == '0':
                    score += 1
            for j in s[i:]:
                if j == '1':
                    score += 1
            list_score.append(score)
        return max(list_score)
