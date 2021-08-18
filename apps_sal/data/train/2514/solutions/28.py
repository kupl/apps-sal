from collections import Counter


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1, arr2 = Counter(arr1), set(arr2)

        res = 0
        for num in arr1:
            target = range(num - d, num + d + 1)
            if not arr2.intersection(target):
                res += arr1[num]

        return res
