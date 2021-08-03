class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        from copy import deepcopy
        from heapq import heapify

        v = deepcopy(arr)

        for i in range(len(arr) - 2, -1, -1):
            s = deepcopy(v[i + 1])
            heapify(s)
            min1 = s[0]
            min2 = min(s[1], s[2])
            # print(min1,min2)
            for j in range(len(arr[0])):

                if v[i + 1][j] != min1:
                    v[i][j] += min1
                else:
                    v[i][j] += min2

        return min(v[0])
