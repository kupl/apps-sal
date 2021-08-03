class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        sortedA = sorted(A)

        for i in range(len(sortedA) - 3, -1, -1):
            if sortedA[i + 2] < (sortedA[i] + sortedA[i + 1]):
                return sum(sortedA[i:i + 3])
        return 0
