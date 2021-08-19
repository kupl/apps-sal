class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                for k in range(j, len(arr)):
                    if 0 <= i < j < k < len(arr) and abs(arr[i] - arr[j]) <= a and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                        x = (arr[i], arr[j], arr[k])
                        ans.append(x)
        if len(arr) == 0:
            return 0
        return len(ans)
