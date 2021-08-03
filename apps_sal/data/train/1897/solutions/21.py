class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        ans = []

        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):

            prefix[i] = prefix[i - 1] ^ arr[i]
        for q in queries:
            l, r = q
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] ^ prefix[l - 1])
        return ans
