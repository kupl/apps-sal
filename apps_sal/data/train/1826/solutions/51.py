class Solution:
    def getArrIJ(self, i: int, j: int, arr: List[List[int]]) -> int:
        if i >= len(arr) and j >= len(arr[0]):
            return arr[len(arr) - 1][len(arr[0]) - 1]
        if i >= len(arr):
            return arr[len(arr) - 1][j]
        if j >= len(arr[0]):
            return arr[i][len(arr[0]) - 1]

        if i < 0 and j < 0:
            return arr[0][0]
        if i < 0:
            return arr[0][j]
        if j < 0:
            return arr[i][0]
        
        return arr[i][j]
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        res = []
        for i in range(K + 1):
            res.append([0] * (n + 2 * (K + 1)))
        for i in range(m):
            res.append([0] * (K + 1) + mat[i] + [0] * (K + 1))
        for i in range(K + 1):
            res.append([0] * (n + 2 * (K + 1)))

        for i in range(1,m+2*(K+1)):
            for j in range(1,n+2*(K+1)):
                res[i][j] = res[i][j] + res[i-1][j] + res[i][j - 1] - res[i - 1][j - 1]

        # print(res)       
        for i in range(K+1,m+K+1):
            for j in range(K+1,n+K+1):
                # print(f'mat[{i-K}][{j-K}] = res[{i + K}][{j + K}] - (res[{i + K}][{j - K - 1}] + res[{i - K - 1}][{j + K}] - res[{i - K - 1}][{j - K - 1}])')
                mat[i-K-1][j-K-1] = res[i + K][j + K] - (res[i + K][j - K - 1] + res[i - K - 1][j + K] - res[i - K - 1][j - K - 1])
        return mat
        

