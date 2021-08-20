class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if len(arr) < 3:
            return 0
        good_trip = []
        for i in range(0, len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            good_trip.append([arr[i], arr[j], arr[k]])
        return len(good_trip)
