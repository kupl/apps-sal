class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        nums = [[0] * len(mat[0]) for _ in range(len(mat))]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if col == 0:
                    nums[row][col] = mat[row][col]
                else:
                    if mat[row][col] == 0:
                        nums[row][col] = 0
                    else:
                        nums[row][col] = nums[row][col - 1] + 1
        res = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                Min = nums[row][col]
                k = row
                while(k >= 0):
                    if nums[k][col] == 0:
                        break
                    Min = min(nums[k][col], Min)
                    res += Min
                    k -= 1
        return res
