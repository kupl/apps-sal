class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        b = [arr[0]]
        for a in arr[1:]:
            b.append(b[-1] ^ a)

        ans = []
        for q in queries:
            r = b[q[1]]
            if q[0] > 0:
                r ^= b[q[0] - 1]
            ans.append(r)

        return ans
