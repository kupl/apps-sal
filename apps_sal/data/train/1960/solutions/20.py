from collections import OrderedDict


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ordered = OrderedDict.fromkeys(list(range(1, m + 1)))
        result = []
        for query in queries:
            idx = 0
            for key in ordered:
                if key == query:
                    break
                idx += 1
            result.append(idx)
            ordered.move_to_end(query, last=False)
        return result
