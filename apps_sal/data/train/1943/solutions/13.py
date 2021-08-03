class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # time O(M+N) space O(M+N)
        result = []
        i = j = 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                result.append([lo, hi])

            # remove interval with smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return result
#         i, j, result= 0, 0, []
#         while i<len(A) and j<len(B):
#             # find overlap or not
#             if A[i][1] < B[j][0]:
#                 i+=1
#             elif B[j][1] < A[i][0]:
#                 j+=1
#             else:
#                 # merged interval condition: max of start index, min of end index
#                 result.append((max(A[i][0], B[j][0]), min(A[i][1], B[j][1])))
#                 if B[j][1] <= A[i][1]:
#                     j+=1
#                 else:
#                     i+=1

#         return result
