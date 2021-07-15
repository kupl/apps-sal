class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(len(arr)-2, -1, -1):
            a = sorted([arr[i+1][j], j] for j in range(len(arr[0])))
            for j in range(len(arr[0])):
                for v, idx in a:
                    if idx != j:
                        arr[i][j] += v
                        break
        return min(arr[0])
