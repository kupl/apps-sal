class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        l = len(arr)
        for i in range(l):
            for j in range(l):
                for k in range(l):
                    if i < j < k:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                            res += 1
        return res
