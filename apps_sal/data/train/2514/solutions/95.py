class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c = list(set([i for i in arr1 for j in arr2 if abs(i-j) <= d ]))
        i = len(arr1)
        for j in c:
            i -= arr1.count(j)
        return i

