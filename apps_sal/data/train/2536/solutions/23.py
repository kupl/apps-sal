class Solution:
    def findLucky(self, arr: List[int]) -> int:
        import collections

# arr=[2,2,2,3,3]
        return max([i for i, j in collections.Counter(arr).items() if i == j], default=-1)
