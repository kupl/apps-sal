class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        ht = [arr[0]]
        for i in range(1, len(arr)):
            ht.append(ht[-1] ^ arr[i])

        for i, j in queries:
            ans.append(ht[j] ^ (ht[i - 1] if i > 0 else 0))
        return ans
