import collections
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 1
        orig = collections.defaultdict(int)
        orig_to_xor = {}
        for row in matrix:
            curr_orig = int(''.join([str(c) for c in row]), 2)
            curr_xor = int(''.join([str(1-c) for c in row]), 2)
            orig[curr_orig] += 1
            orig_to_xor[curr_orig] = curr_xor
        for curr_orig, curr_xor in orig_to_xor.items():
            ans = max(orig[curr_orig] + orig[curr_xor], ans) if curr_orig!=curr_xor else max(orig[curr_orig], ans)
        return ans
