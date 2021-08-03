class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        mat = [[abs(arr[i] - arr[j]) for j in range(len(arr))] for i in range(len(arr))]
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if mat[i][j] > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if mat[j][k] <= b and mat[i][k] <= c:
                        ans += 1
        return ans
