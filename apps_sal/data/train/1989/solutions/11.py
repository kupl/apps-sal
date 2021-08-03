class Solution:
    def longestAwesome(self, s: str) -> int:
        index = [-1] + [len(s)] * 1023
        ans = 0
        bit = 0
        for idx, c in enumerate(s):
            bit ^= 1 << ord(c) - ord('0')
            # if bit in index:
            #     ans = max(ans, idx-index[candidate])
            # else:
            #     index[bit]=idx
            # for i in range(10):
            #     candidate = bit^(1<<i)
            #     if candidate in index:
            #         ans = max(ans, idx-index[candidate])
            ans = max([ans, idx - index[bit]] + [idx - index[bit ^ (1 << j)] for j in range(10)])
            index[bit] = min(index[bit], idx)
        return ans
