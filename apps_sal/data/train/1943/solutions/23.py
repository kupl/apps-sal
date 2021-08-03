class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i, j, ans = 0, 0, []
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            if not (a[1] < b[0] or a[0] > b[1]):
                ans.append([max(a[0], b[0]), min(a[1], b[1])])
            if a[1] >= b[1]:
                j += 1
            elif b[1] >= a[1]:
                i += 1
        return ans
