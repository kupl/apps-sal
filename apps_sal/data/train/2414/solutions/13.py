class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        totallen = len(arr)
        res = 0
        for i in range(totallen - 2):
            for j in range(i + 1, totallen - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, totallen):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
        return res
