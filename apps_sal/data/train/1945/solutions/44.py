import collections


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 1
        orig = collections.defaultdict(int)
        orig_to_xor = {}
        for row in matrix:
            curr_orig = 0
            curr_xor = 0
            for i, c in enumerate(row):
                curr_orig ^= c << i
                curr_xor ^= (1 - c) << i
            orig[curr_orig] += 1
            orig_to_xor[curr_orig] = curr_xor
        for curr_orig, curr_xor in orig_to_xor.items():
            ans = max(orig[curr_orig] + orig[curr_xor], ans) if curr_orig != curr_xor else max(orig[curr_orig], ans)
        return ans
