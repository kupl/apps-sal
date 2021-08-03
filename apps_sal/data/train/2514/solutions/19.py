class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        dists = []
        for x in arr1:
            dists.append([abs(x - y) > d for y in arr2])

        return sum([all(x) for x in dists])
