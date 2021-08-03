class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ite1 = 0
        ite2 = 0
        lenA = len(A)
        lenB = len(B)

        ans = []
        while ite1 < lenA and ite2 < lenB:
            curA = A[ite1]
            curB = B[ite2]

            s, e = max(curA[0], curB[0]), min(curA[1], curB[1])
            if s <= e:
                ans.append([s, e])
            if curA[1] > curB[1]:
                ite2 += 1
            elif curA[1] < curB[1]:
                ite1 += 1
            else:
                ite1 += 1
                ite2 += 1

        return ans
