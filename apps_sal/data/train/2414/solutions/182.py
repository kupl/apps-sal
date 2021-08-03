class Solution:
    def isGood(self, ai, aj, ak, a, b, c, length) -> bool:
        if not abs(ai - aj) <= a:
            return False
        elif not abs(aj - ak) <= b:
            return False
        elif not abs(ai - ak) <= c:
            return False
        else:
            return True

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    res += int(self.isGood(arr[i], arr[j], arr[k], a, b, c, len(arr)))
        return res
