class Solution:
    def average(self, arr: List[int]) -> float:
        return (sum(arr) - min(arr) - max(arr)) / (len(arr) - 2)
