def bs(a, t, d):
    (l, r) = (0, len(a))
    while l < r:
        mid = l + (r - l) // 2
        if abs(a[mid] - t) <= d:
            return 0
        elif a[mid] > t:
            r = mid
        else:
            l = mid + 1
    return 1


class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        total = 0
        arr2.sort()
        for n in arr1:
            total += bs(arr2, n, d)
        return total
