class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        somme = 0
        for row in grid:
            for el in row:
                if el < 0:
                    somme += 1
        return somme
