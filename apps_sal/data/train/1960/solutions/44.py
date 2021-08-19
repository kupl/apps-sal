class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        l = [i for i in range(1, m + 1)]
        ans = []
        for q in queries:
            d = {}
            for (index, element) in enumerate(l):
                d[element] = index
            ans.append(d[q])
            x = l.pop(d[q])
            l = [x] + l
        return ans
