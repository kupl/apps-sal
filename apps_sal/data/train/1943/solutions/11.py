class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        NA = len(A)
        NB = len(B)
        if NA == 0 or NB == 0:
            return []

        pA = 0
        pB = 0
        res = []
        while pA<NA and pB<NB:
            sA = A[pA][0]
            eA = A[pA][1]
            sB = B[pB][0]
            eB = B[pB][1]
            if sA<=sB:
                if eA>=sB:
                    res.append([sB,min(eA,eB)])
            else:
                if eB>=sA:
                    res.append([sA,min(eA,eB)])
            if eA<eB:
                pA += 1
            elif eA == eB:
                pA += 1
                pB += 1
            else:
                pB += 1


        return res
