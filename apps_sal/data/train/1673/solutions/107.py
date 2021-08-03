class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        min_index = 0
        secondmn_index = 0
        temp = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
        temp[0] = arr[0][:]
        for i in range(1, len(arr)):
            min_index = 0
            secondmn_index = 1
            for j in range(len(arr)):
                if temp[i - 1][min_index] > temp[i - 1][j]:
                    secondmn_index = min_index
                    min_index = j
                elif temp[i - 1][secondmn_index] > temp[i - 1][j] and j != min_index:
                    secondmn_index = j
            for j in range(len(arr)):
                if j != min_index:
                    temp[i][j] = arr[i][j] + temp[i - 1][min_index]
                else:
                    temp[i][j] = arr[i][j] + temp[i - 1][secondmn_index]
        print(temp)
        return min(temp[len(temp) - 1])
