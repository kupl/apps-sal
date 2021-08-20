class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        temp_array = copy.deepcopy(arr[0])
        for i in range(1, len(arr)):
            print(temp_array)
            temp_array_new = [0] * len(arr)
            for j in range(0, len(arr)):
                mins = [temp_array[k] for k in range(len(arr)) if k != j]
                temp_array_new[j] = min(mins) + arr[i][j]
            temp_array = copy.deepcopy(temp_array_new)
        print(temp_array)
        return min(temp_array)
