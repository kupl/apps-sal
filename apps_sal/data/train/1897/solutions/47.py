class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        xors = []
        x = 0
        for num in arr:
            x ^= num
            xors.append(x)

        ans = []
        for i, j in queries:

            if i == 0:
                ans.append(xors[j])
            else:
                ans.append(xors[j] ^ xors[i - 1])

        return ans
