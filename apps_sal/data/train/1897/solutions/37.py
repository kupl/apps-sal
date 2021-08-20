class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        curr = 0
        cum_sum = []
        res = []
        for n in arr:
            curr ^= n
            cum_sum.append(curr)
        for (start, end) in queries:
            x = cum_sum[end] ^ (cum_sum[start - 1] if start > 0 else 0)
            res.append(x)
        return res
