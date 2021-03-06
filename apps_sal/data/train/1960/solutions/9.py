class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        original = list(range(1, m + 1))
        results = []
        for q in queries:
            res = 0
            for (ind, el) in enumerate(original):
                if el == q:
                    res = ind
                    break
            results.append(res)
            temp = original.pop(res)
            original = [temp] + original
        return results
