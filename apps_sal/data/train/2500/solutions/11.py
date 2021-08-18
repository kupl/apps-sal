class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        consec_count_per_letter = 1
        prev_letter = s[0]

        if len(s) == 1:
            return 1

        for i in range(1, len(s)):
            if s[i] == prev_letter:
                consec_count_per_letter += 1
            else:
                consec_count_per_letter = 1

            prev_letter = s[i]
            ans = max(ans, consec_count_per_letter)

        return ans
