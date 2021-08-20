class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(A) and j < len(B):
            if A[i][0] >= B[j][0] and A[i][1] <= B[j][1]:
                ans.append([A[i][0], A[i][1]])
                i += 1
            elif B[j][0] >= A[i][0] and B[j][1] <= A[i][1]:
                ans.append([B[j][0], B[j][1]])
                j += 1
            elif A[i][1] >= B[j][0] and A[i][0] <= B[j][0]:
                ans.append([B[j][0], A[i][1]])
                i += 1
            elif B[j][1] >= A[i][0] and B[j][0] <= A[i][0]:
                ans.append([A[i][0], B[j][1]])
                j += 1
            elif B[j][1] < A[i][0]:
                j += 1
            elif A[i][1] < B[j][0]:
                i += 1
        return ans
