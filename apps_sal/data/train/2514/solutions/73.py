import numpy

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        s = len(arr1)
        n2 = len(arr2)
        for x in arr1:
            k = numpy.searchsorted(arr2, x)
            if k < n2 and arr2[k] - x <= d:
                s -= 1
            else:
                if k >= 1 and x - arr2[k - 1] <= d:
                    s -= 1
        return s
                

