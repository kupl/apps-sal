class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        
        \"\"\"
        Returns the tuples (fp_sum, fp_sum_2) each of the form
        (col, value) where col is the col the falling path sum
        starts from and value is the falling path sum's value.
        fp_sum is the true min falling path sum for the row and
        fp_sum_2 is the SECOND-to-min falling path sum for the
        row. That way we can guarantee an optimal continuation
        for the row before since the element with the same col
        as fp_sum can just continue locally with fp_sum_2.
        \"\"\"
        @lru_cache(maxsize=None)
        def min_fp_sums(row):
            fp_sum, fp_sum_2 = ((-1, 0), (-1, 0)) if row == n - 1 else min_fp_sums(row + 1)
            min_fp_sum, min_fp_sum_2 = ((-1, math.inf), (-1, math.inf))
            for col, num in enumerate(arr[row]):
                value = num + (fp_sum if col != fp_sum[0] else fp_sum_2)[1]
                if value < min_fp_sum[1]:
                    min_fp_sum_2 = min_fp_sum
                    min_fp_sum = (col, value)
                elif value < min_fp_sum_2[1]:
                    min_fp_sum_2 = (col, value)
            return min_fp_sum, min_fp_sum_2
            
        return min_fp_sums(0)[0][1]
