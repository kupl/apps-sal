class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()
        ans = 0

        for base in arr1:
            count = 0
            idx = 0
            while idx < len(arr2) and base > arr2[idx]:
                idx += 1
            if idx == 0:
                ans += abs(base - arr2[idx]) > d
            elif idx == len(arr2):
                ans += abs(base - arr2[idx - 1]) > d
            else:
                ans += ((abs(base - arr2[idx]) > d) and (abs(base - arr2[idx - 1]) > d))

        return ans
