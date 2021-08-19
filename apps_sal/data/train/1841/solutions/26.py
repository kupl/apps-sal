class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        median = sorted(arr)[(len(arr) - 1) // 2]
        median_sorted_array = sorted(((i, val) for (i, val) in enumerate(arr)), key=lambda x: (abs(x[1] - median), x[1]), reverse=True)
        return [x[1] for x in median_sorted_array[:k]]
