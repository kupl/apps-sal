from collections import deque


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        N = len(locations)
        M = 10 ** 9 + 7
        adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                adj_matrix[i][j] = abs(locations[i] - locations[j])
                adj_matrix[j][i] = abs(locations[i] - locations[j])

        # q = deque()
        # ans = 0
        # q.append((start, fuel))
        # while len(q) > 0:
        #     location, fuel_left = q.popleft()
        #     # print(location, fuel_left)
        #     if location == finish:
        #         ans = (ans + 1) % M
        #     for dst in range(N):
        #         if dst == location:
        #             continue
        #         if adj_matrix[location][dst] + adj_matrix[dst][finish] <= fuel_left:
        #             q.append((dst, fuel_left - adj_matrix[location][dst]))
        memo = {}

        def dfs(location, fuel_left):
            if fuel_left < 0:
                return 0
            if (location, fuel_left) in memo:
                return memo[(location, fuel_left)] % M

            if location == finish:
                cnt = 1
            else:
                cnt = 0
            for dst in range(N):
                if dst == location:
                    continue
                if adj_matrix[location][dst] + adj_matrix[dst][finish] <= fuel_left:
                    cnt += dfs(dst, fuel_left - adj_matrix[location][dst])
            memo[(location, fuel_left)] = cnt
            return cnt

        return dfs(start, fuel) % M
