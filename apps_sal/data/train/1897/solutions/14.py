class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        a = 0
        n = len(arr)
        for i in range(n):
            a ^= arr[i]
            arr[i] = a
        ans = []
        for i, j in queries:
            if i == 0:

                ans.append(arr[j])
            else:
                ans.append(arr[j] ^ arr[i - 1])
        return ans
