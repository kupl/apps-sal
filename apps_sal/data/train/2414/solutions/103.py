class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        self.counter = 0
        for i in range(0, len(arr)-2):
            for k in range(2, len(arr)):
                if abs(arr[i]-arr[k]) <= c and i < k-1:
                    for j in range (1, len(arr)-1):
                        if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and i < j < k:
                            self.counter += 1
        return self.counter
