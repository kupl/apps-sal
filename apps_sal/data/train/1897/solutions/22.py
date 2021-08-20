class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        precompute = []
        xor = 0
        for num in arr:
            xor ^= num
            precompute.append(xor)
        ans = []
        for (s, e) in queries:
            if s == 0:
                ans += [precompute[e]]
            else:
                ans += [precompute[e] ^ precompute[s - 1]]
        return ans
