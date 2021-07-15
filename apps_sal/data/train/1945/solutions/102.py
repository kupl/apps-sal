class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        orig = []
        xor = []
        for row in matrix:
            curr_orig = ''
            curr_xor = ''
            for c in row:
                curr_orig += str(c)
                curr_xor += str(1-c)
            orig.append(int(curr_orig, 2))
            xor.append(int(curr_xor, 2))
        for i in range(len(matrix)):
            curr = 1
            for j in range(i+1, len(matrix)):
                is_complement = xor[i] == orig[j]
                is_equal = orig[i] == orig[j]
                curr += int(is_complement or is_equal)
            ans = max(curr, ans)
        return ans
