class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        orig = [int(''.join([str(c) for c in row]), 2) for row in matrix]
        xor = [int(''.join([str(1-c) for c in row]), 2) for row in matrix]
        for i in range(len(matrix)):
            curr = 1
            for j in range(i+1, len(matrix)):
                is_complement = xor[i] == orig[j]
                is_equal = orig[i] == orig[j]
                curr += int(is_complement or is_equal)
            ans = max(curr, ans)
        return ans
