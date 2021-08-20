class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        self.counter = 0
        for i in range(0, len(arr) - 2):
            for k in range(2, len(arr)):
                if i < k - 1 and abs(arr[i] - arr[k]) <= c:
                    for j in range(1, len(arr) - 1):
                        if i < j < k and abs(arr[i] - arr[j]) <= a and (abs(arr[j] - arr[k]) <= b):
                            self.counter += 1
        return self.counter
