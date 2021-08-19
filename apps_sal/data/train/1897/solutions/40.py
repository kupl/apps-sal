class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        cur = 0
        for num in arr:
            cur = cur ^ num
            prefix.append(cur)
        ans = []
        for (l, r) in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[l - 1] ^ prefix[r])
        return ans
