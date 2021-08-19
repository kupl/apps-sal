class Solution:

    def maxPower(self, s: str) -> int:
        n = len(s)
        count = 0
        res = s[0]
        cur_count = 1
        for i in range(n):
            if i < n - 1 and s[i] == s[i + 1]:
                cur_count += 1
            else:
                if cur_count > count:
                    count = cur_count
                    res = s[i]
                cur_count = 1
        return count
