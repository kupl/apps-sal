class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i = 0
        res = 0
        while i <= len(arr) - 3:
            j = i + 1
            while j <= len(arr) - 2:
                k = j + 1
                while k <= len(arr) - 1:
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                        res += 1
                    k += 1
                j += 1
            i += 1
        return res
