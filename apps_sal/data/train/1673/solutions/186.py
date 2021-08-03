class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        nr = len(arr)
        nc = len(arr[0])

        store = arr[:]

        result = 0

        for i in range(nr):

            for j in range(nc):

                if i > 0:

                    store[i][j] = min(store[i - 1][:j] + store[i - 1][j + 1:]) + arr[i][j]

        print(store)

        return min(store[nr - 1])
