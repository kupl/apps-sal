class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        P = []
        for i in range(m):
            P.append(i + 1)
        for i in range(len(queries)):
            a = P.index(queries[i])
            ans.append(a)
            b = P.pop(a)
            P = [b] + P
        return ans
