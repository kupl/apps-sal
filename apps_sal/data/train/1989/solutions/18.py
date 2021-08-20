class Solution:

    def longestAwesome(self, s: str) -> int:
        tmp = 0
        pos_map = {0: -1}
        ans = 1
        for i in range(len(s)):
            tmp ^= 1 << int(s[i])
            if tmp in pos_map:
                ans = max(ans, i - pos_map[tmp])
            for x in range(10):
                another_tmp = tmp ^ 1 << x
                if another_tmp in pos_map:
                    ans = max(ans, i - pos_map[another_tmp])
            if tmp not in pos_map:
                pos_map[tmp] = i
        return ans
