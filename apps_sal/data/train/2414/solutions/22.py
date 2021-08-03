class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        ctr = 0
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                for k in range(j + 1, size):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ctr += 1
        return ctr
