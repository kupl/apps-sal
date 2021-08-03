class Solution:
    def longestAwesome(self, s: str) -> int:
        idxs = [1e9 for _ in range(1024)]
        idxs[0] = -1
        ans = 0
        mask = 0
        for i, ch in enumerate(s):
            mask ^= 1 << ord(ch) - ord('0')
            ans = max([ans, i - idxs[mask]] + [i - idxs[mask ^ (1 << j)] for j in range(10)])
            idxs[mask] = min(idxs[mask], i)
        return ans
