class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        d = 0
        e = len(arr)
        for i in range(e):
            for j in range(e):
                for k in range(e):
                    if k > j and j > i:
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            d += 1
        return d
