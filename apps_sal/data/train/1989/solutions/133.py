class Solution:
    def longestAwesome(self, s: str) -> int:
        # first we need to create a index list
        index = [-1] + [len(s)] * 1023
        # intialize a prefix and ret
        prefix, ans = 0, 0

        # then start for loop the string s
        for i, c in enumerate(s):  # i is index and c is char
            prefix = prefix ^ (1 << (ord(c) - ord('0')))
            print(prefix)
            ans = max(ans, i - index[prefix])

            # and we need to check all the odd bit (1 is allowed)
            for j in range(10):
                ans = max(ans, i - index[prefix ^ (1 << j)])

            index[prefix] = min(i, index[prefix])

        return ans
