class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_cnt = r_cnt = 0
        output = 0
        for i in range(len(s)):
            if s[i] == 'R':
                r_cnt += 1
            else:
                l_cnt += 1
            if l_cnt == r_cnt:
                output += 1
        return output
