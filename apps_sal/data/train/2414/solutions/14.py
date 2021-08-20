class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        def isGood(i, j, a):
            return abs(arr[i] - arr[j]) <= a
        ret = 0
        if not arr:
            return ret
        n = len(arr)
        for i in range(0, n):
            for j in range(i + 1, n):
                if isGood(i, j, a):
                    for k in range(j + 1, n):
                        if isGood(j, k, b) and isGood(i, k, c):
                            ret += 1
        return ret
