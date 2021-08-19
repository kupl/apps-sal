class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        # direct merge intervals approach
        # problem : https://leetcode.com/problems/interval-list-intersections/
        # T = O(M + N) # the lengths of A,B
        # S = O(M + N)

        ans = []
        i, j = 0, 0  # two pointers to keep track of A,B

        while i < len(A) and j < len(B):

            # first the get the start pointer for the intersection
            # the start point is the fatherst away is the right one
            lo = max(A[i][0], B[j][0])

            # then get the pos, where the intervel ends first
            # eighter in A or B
            high = min(A[i][1], B[j][1])

            if lo <= high:
                ans.append([lo, high])

            # remove the interval with the smallest end point
            if A[i][1] < B[j][1]:
                # consider next sample in A
                i += 1
            else:
                # consider next sample in B
                j += 1

        return ans
