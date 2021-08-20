class Solution:

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        op = []
        hashP = {}
        for (i, p) in enumerate(P):
            hashP[p] = i
        for query in queries:
            idx = hashP[query]
            if idx != 0:
                for key in hashP:
                    if key == query:
                        hashP[key] = 0
                    elif hashP[key] < idx:
                        hashP[key] += 1
            op.append(idx)
        return op
