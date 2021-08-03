class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    conditions = [
                        abs(arr[i] - arr[j]) <= a,
                        abs(arr[j] - arr[k]) <= b,
                        abs(arr[i] - arr[k]) <= c
                    ]
                    if all(conditions):
                        ans += 1
        return ans
