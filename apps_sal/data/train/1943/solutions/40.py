class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        (res, a, b) = ([], 0, 0)
        while a < len(A) and b < len(B):
            if A[a][1] < B[b][0]:
                a += 1
            elif B[b][1] < A[a][0]:
                b += 1
            else:
                res.append([max(A[a][0], B[b][0]), min(A[a][1], B[b][1])])
                if A[a][1] < B[b][1]:
                    a += 1
                else:
                    b += 1
        return res
