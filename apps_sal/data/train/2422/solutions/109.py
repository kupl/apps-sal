class Solution:
    def maxProduct(self, L: List[int]) -> int:
        max = 0
        x = 0
        y = 0
        for i in range(len(L)):
            for j in range(len(L)):
                if L[i] * L[j] > max and i != j:
                    max = L[i] * L[j]
                    x, y = i, j
        return (L[x] - 1) * (L[y] - 1)
