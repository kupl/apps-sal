class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        scount = 0
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    da = abs(arr[i] - arr[j])
                    db = abs(arr[j] - arr[k])
                    dc = abs(arr[i] - arr[k])
                    if da <= a and db <= b and (dc <= c):
                        scount += 1
        return scount
