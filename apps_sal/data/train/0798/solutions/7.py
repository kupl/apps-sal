# cook your dish here

# import time
import collections


def solve(n, m, grid, charms):
    newGrid = [[[val, False] for val in row] for row in grid]

    for x, y, k in charms:
        newGrid[x][y][1] = True
        queue = collections.deque([(x, y, 0)])
        visited = set()
        visited.add((x, y))

        while queue:
            currX, currY, cost = queue.popleft()

            for delX, delY in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                newX, newY = currX + delX, currY + delY

                if 0 <= newX < n and 0 <= newY < n and (newX, newY) not in visited and cost < k:
                    newGrid[newX][newY][1] = True
                    visited.add((newX, newY))

                    if cost + 1 <= k:
                        queue.append((newX, newY, cost + 1))

    # for row in newGrid:
    #     print(row)

    NEG_INF = float("-inf")

    dp = [[NEG_INF if not newGrid[i][j][1]
           else newGrid[i][j][0] for j in range(n)] for i in range(n)]

    # print("After")
    # for row in dp:
    #     for val in row:
    #         if val == NEG_INF:
    #             print(0, end=" ")
    #         else:
    #             print(1, end=" ")
    #     print()

    # for row in dp:
    #     print(row)

    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])

    # print("After")
    # for row in dp:
    #     print(row)

    return (dp[n-1][n-1] != NEG_INF, dp[n-1][n-1])


[n, m] = list(map(int, input().strip().split()))

grid = []

for i in range(n):
    row = list(map(int, input().strip().split()))
    grid.append(row)

charms = []

for i in range(m):
    [x, y, k] = list(map(int, input().strip().split()))

    charms.append((x-1, y-1, k))

# start_time = time.time()
ans = solve(n, m, grid, charms)

if ans[0]:
    print("YES")
    print(ans[1])
else:
    print("NO")

# print("--- %s seconds ---" % (time.time() - start_time))

