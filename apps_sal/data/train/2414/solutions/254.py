class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i = 0
        res = 0
        while i < len(arr):
            j = i + 1
            while j < len(arr):
                if abs(arr[j] - arr[i]) <= a:
                    k = j + 1
                    while k < len(arr):
                        if abs(arr[k] - arr[j]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
                        k += 1
                j += 1

            i += 1

        return res
