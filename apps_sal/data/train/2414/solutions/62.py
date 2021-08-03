class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

        res = 0

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if j <= i:
                    continue
                for k in range(j, len(arr)):
                    if k <= i or k <= j:
                        continue

                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1

        return res
