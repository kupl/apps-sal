class Solution:

    def processQueries(self, queries, m):
        P = list(range(1, m + 1))
        return [n for x in queries if not P.insert(0, P.pop((n := P.index(x))))]
