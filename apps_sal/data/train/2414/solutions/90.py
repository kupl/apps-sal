class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if i == j or j == k or i == k or (i == j == k):
                        continue
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and (abs(arr[i] - arr[k]) <= c):
                        cnt += 1
        return cnt
