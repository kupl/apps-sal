class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        numGoodTrips = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if self.isGoodTriplet(arr, i, j, k, a, b, c):
                        numGoodTrips += 1
        return numGoodTrips

    def isGoodTriplet(self, arr: List[int], i: int, j: int, k: int, a: int, b: int, c: int) -> bool:
        return i < j and j < k and k < len(arr) and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c
