class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        # kruskal:
        n = len(A)
        distance_arr = []
        for i in range(n):
            for j in range(i + 1, n):
                distance_arr.append([abs(A[j][0] - A[i][0]) + abs(A[j][1] - A[i][1]), i, j])

        distance_arr.sort()
        root = [i for i in range(n)]

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        cnt = 0
        sm = 0
        for dis, x, y in distance_arr:
            if find(x) == find(y):
                continue
            root[find(x)] = find(y)
            cnt += 1
            sm += dis
            if cnt == n - 1:
                break
        return sm
