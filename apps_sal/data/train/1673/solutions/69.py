class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for i in range(1, len(arr)):
            for j in range(len(arr[0])):
                above = set()
                for k in range(len(arr[0])):
                    if k != j:
                        above.add(arr[i - 1][k])
                # print(above)
                arr[i][j] = arr[i][j] + min(above)

        # for row in arr:
            # print(row)
        return min(arr[-1])
