class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        current = list(range(m, 1 - 1, -1))
        ans = list()
        for query in queries:
            ind = m - 1 - current.index(query)
            current.remove(query)
            current.append(query)
            ans.append(ind)
        return ans
