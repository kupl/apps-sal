class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        lookup = {key: key - 1 for key in range(1, m + 1)}
        ans = []
        for query in queries:
            temp = lookup[query]
            ans.append(temp)
            for (key, val) in lookup.items():
                if key == query:
                    lookup[key] = 0
                elif val < temp:
                    lookup[key] += 1
        return ans
