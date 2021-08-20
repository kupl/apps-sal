class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        diff = [sorted(heights)[k] - heights[k] for k in range(len(heights))]
        move = 0
        for x in diff:
            if x != 0:
                move = move + 1
        return move
