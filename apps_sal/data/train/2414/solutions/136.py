class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good_count = 0
        i = 0
        j = 1
        k = 2
        if len(arr) > 2:
            while i + 2 < len(arr):

                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    good_count += 1
                if k != len(arr) - 1:
                    k += 1
                elif k == len(arr) - 1 and j + 1 != k:
                    j += 1
                    k = j + 1
                elif j == len(arr) - 2:
                    i += 1
                    j = i + 1
                    k = j + 1

        return good_count
