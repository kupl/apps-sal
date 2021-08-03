class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        out = 0
        for i in range(length - 1 - 1):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        out += 1
        return out
