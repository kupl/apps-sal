class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        A = []
        for i in range(n):
            A.append([float('inf')] * n)
        for i in range(len(A)):
            A[i][i] = 0
        for i in edges:
            A[i[0]][i[1]] = i[2]
            A[i[1]][i[0]] = i[2]
        for k in range(n):
            for i in range(len(A)):
                for j in range(len(A[i])):
                    if i == j or i == k or j == k:
                        continue
                    A[i][j] = min(A[i][j], A[i][k] + A[k][j])
        print(A)
        minc = float('inf')
        city = n - 1
        for i in range(len(A)):
            cnt = 0
            for j in range(len(A[i])):
                if A[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= minc:
                minc = cnt
                city = i
        return city
