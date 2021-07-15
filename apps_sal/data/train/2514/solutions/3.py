class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        bound = [(n+d,n-d) for n in arr2]
        out = 0
        for n in arr1:
            if any([ Up >= n >= Low for Up, Low in bound]):
                out += 1
        return len(arr1) - out

