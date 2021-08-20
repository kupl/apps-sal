class Solution:

    def searchMatrix(self, matrix, target):
        ans = False
        if matrix == [[]] or matrix == []:
            return ans
        ans = self.check(matrix, target, ans)
        return ans

    def check(self, matrix, target, ans):
        if ans == True:
            return ans
        for i in range(min(len(matrix[0]), len(matrix))):
            if target == matrix[i][i]:
                ans = True
                return ans
            elif i + 1 != min(len(matrix[0]), len(matrix)) and target > matrix[i][i] and (target < matrix[i + 1][i + 1]):
                temp = []
                for x in range(i + 1):
                    temp.append(matrix[x][i:])
                ans = self.check(temp, target, ans)
                temp = []
                for x in range(len(matrix) - i):
                    temp.append(matrix[i + x][:i + 1])
                ans = self.check(temp, target, ans)
            else:
                continue
        if target > matrix[min(len(matrix[0]), len(matrix)) - 1][min(len(matrix[0]), len(matrix)) - 1]:
            if len(matrix[0]) == len(matrix):
                return ans
            elif len(matrix[0]) > len(matrix):
                temp = []
                for x in range(len(matrix)):
                    temp.append(matrix[x][len(matrix):])
                print(temp)
                ans = self.check(temp, target, ans)
            else:
                temp = []
                for x in range(len(matrix) - len(matrix[0])):
                    temp.append(matrix[len(matrix[0]) + x])
                ans = self.check(temp, target, ans)
        return ans
        '\n         :type matrix: List[List[int]]\n         :type target: int\n         :rtype: bool\n         '
