class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        n = len(arr)
        for i1 in range(n):
            for i2 in range(i1 + 1, n):
                for i3 in range(i2 + 1, n):
                    if abs(arr[i1] - arr[i2]) <= a and abs(arr[i2] - arr[i3]) <= b and (abs(arr[i1] - arr[i3]) <= c):
                        result += 1
        return result
