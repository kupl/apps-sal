class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        goodcount = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                k = j + 1
                while k < len(arr):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                        goodcount += 1
                    k += 1
        return goodcount
