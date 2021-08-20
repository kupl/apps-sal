class Solution:

    def maxScore(self, s: str) -> int:

        def countchar(given, char):
            count = 0
            for x in given:
                if x == char:
                    count += 1
            return count
        maxans = 0
        for i in range(len(s) - 1):
            ans = 0
            if s[:i + 1]:
                leftcount = countchar(s[:i + 1], '0')
                ans += leftcount
            if s[i + 1:]:
                rightcount = countchar(s[i + 1:], '1')
                ans += rightcount
            maxans = max(maxans, ans)
        return maxans
