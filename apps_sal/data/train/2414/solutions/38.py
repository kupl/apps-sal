class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count, n = 0, len(arr)

        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x, y, z = arr[i], arr[j], arr[k]
                    if abs(x - y) <= a and abs(y - z) <= b and abs(z - x) <= c:
                        count += 1

        return count
