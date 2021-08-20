class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        permu = list(range(1, m + 1))
        pos = []
        for i in queries:
            p = permu.index(i)
            pos.append(p)
            for j in range(p - 1, -1, -1):
                permu[j + 1] = permu[j]
            permu[0] = i
        return pos
