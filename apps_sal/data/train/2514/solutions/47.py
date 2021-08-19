class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        i1 = 0
        i2 = 0
        ans = 0
        while i1 < len(arr1):
            while i2 < len(arr2) and arr2[i2] < arr1[i1]:
                i2 += 1
            if i2 == 0:
                ans = ans + 1 if abs(arr2[i2] - arr1[i1]) > d else ans
            elif i2 == len(arr2):
                ans = ans + 1 if abs(arr2[i2 - 1] - arr1[i1]) > d else ans
            else:
                ans = ans + 1 if min(abs(arr2[i2 - 1] - arr1[i1]), abs(arr2[i2] - arr1[i1])) > d else ans
            i1 += 1
        return ans
