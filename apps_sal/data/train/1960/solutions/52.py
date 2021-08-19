class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        current = list(range(m, 1 - 1, -1))

        ans = list()
        for query in queries:
            # O(n)
            ind = m - 1 - current.index(query)

            # O(n)
            current.remove(query)
            # O(1)
            current.append(query)

            ans.append(ind)

        return ans
