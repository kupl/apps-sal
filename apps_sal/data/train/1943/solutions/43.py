class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if self.overlap(A[i], B[j]):
                result.append(self.intersection(A[i], B[j]))
            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1
        return result

    def overlap(self, i1, i2):
        return any([i1[0] <= i2[0] <= i1[1], i1[0] <= i2[1] <= i1[1], i2[0] <= i1[0] <= i2[1], i2[0] <= i1[1] <= i2[1]])

    def intersection(self, i1, i2):
        return [max(i1[0], i2[0]), min(i1[1], i2[1])]
