class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        
        ans = []
        i = j = 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if B[j][1] > A[i][1]:
                i += 1
            elif B[j][1] < A[i][1]:
                j += 1
            else:
                i += 1
                j += 1
        return ans

