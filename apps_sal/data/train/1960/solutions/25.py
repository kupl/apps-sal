class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        rtnlst = []
        P = []
        for n in range(1, m + 1):
            P.append(n)
        for q in queries:
            for p in range(0, len(P)):
                if (P[p] == q):
                    rtnlst.append(p)

            P.pop(rtnlst[-1])
            P = [q] + P

        return rtnlst
