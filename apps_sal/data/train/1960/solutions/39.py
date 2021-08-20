class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        p = [i for i in range(1, m + 1)]
        for query in queries:
            for (index, value) in enumerate(p):
                if value == query:
                    result.append(index)
                    depCounter = index
                    while depCounter > 0:
                        p[depCounter] = p[depCounter - 1]
                        depCounter -= 1
                    p[0] = value
                    break
        return result
