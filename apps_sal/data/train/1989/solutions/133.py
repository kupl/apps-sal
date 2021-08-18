class Solution:
    def longestAwesome(self, s: str) -> int:
        index = [-1] + [len(s)] * 1023
        prefix, ans = 0, 0

        for i, c in enumerate(s):
            prefix = prefix ^ (1 << (ord(c) - ord('0')))
            print(prefix)
            ans = max(ans, i - index[prefix])

            for j in range(10):
                ans = max(ans, i - index[prefix ^ (1 << j)])

            index[prefix] = min(i, index[prefix])

        return ans
