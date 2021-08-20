class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    (x, y, z) = (arr[i], arr[j], arr[k])
                    ans += int(abs(x - y) <= a and abs(y - z) <= b and (abs(x - z) <= c))
        return ans
