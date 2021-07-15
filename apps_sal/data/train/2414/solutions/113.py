class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for x in range(len(arr)):
            for y in range(x+1, len(arr)):
                for z in range(y+1, len(arr)):
                    if (abs(arr[x] - arr[y]) <= a) & (abs(arr[y] - arr[z]) <= b) & (abs(arr[x] - arr[z]) <= c):
                        res += 1
        return res
