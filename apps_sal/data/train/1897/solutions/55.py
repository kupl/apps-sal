class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        px = arr[:]

        for i in range(1, len(px)):
            px[i] ^= px[i - 1]

        res = []

        for q in queries:
            s, e = q[0], q[1]
            r = px[e]

            if s:
                r ^= px[s - 1]
            res.append(r)

        return res
