class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        def helper(arr):
            count = 0
            curr = 0

            for item in arr:

                if item != 1:
                    curr = 0
                else:
                    curr += 1

                count += curr

            return count

        result = 0
        for x1 in range(len(mat)):

            zeros = [1 for x in range(len(mat[0]))]

            for x2 in range(x1, len(mat)):

                for col in range(len(mat[0])):

                    zeros[col] &= mat[x2][col]

                result += helper(zeros)

        return result
