class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        val = float('inf')
        arr = [[val for i in range(0, n)] for j in range(0, n)]

        for x in edges:
            arr[x[0]][x[1]] = x[2]
            arr[x[1]][x[0]] = x[2]

        for i in range(0, n):
            arr[i][i] = 0

        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    if arr[i][j] > arr[i][k] + arr[k][j]:
                        arr[i][j] = arr[i][k] + arr[k][j]

        mn = val
        for i in range(0, n):
            count = 0
            for x in arr[i]:
                if x <= distanceThreshold:
                    count += 1
            if count <= mn:
                mn = count
                ret = i

        return ret
