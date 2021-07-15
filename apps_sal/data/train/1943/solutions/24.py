class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        A.append([math.inf, math.inf])
        B.append([math.inf, math.inf])
        while i < len(A)-1 or j < len(B)-1:
            (i1_s, i1_e), (i2_s, i2_e) = A[i], B[j]
            if i1_e >= i2_s:
                if i1_s <= i2_e:
                    res.append([max(i1_s, i2_s), min(i1_e, i2_e)])
                j += 1
            else:
                if j > 0: j -= 1
                i += 1
        return res

