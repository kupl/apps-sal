class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        copy = deepcopy(arr)
        for row in range(1, len(arr)):
            (min1, ind1, min2, ind2) = (20000, 0, 20000, 0)
            for (i, v) in enumerate(copy[row - 1]):
                if v < min1:
                    min1 = v
                    ind1 = i
            for (i, v) in enumerate(copy[row - 1]):
                if v < min2 and i != ind1:
                    min2 = v
                    ind2 = i
            for col in range(len(arr[0])):
                copy[row][col] += copy[row - 1][ind1] if ind1 != col else copy[row - 1][ind2]
        return min(copy[-1])
