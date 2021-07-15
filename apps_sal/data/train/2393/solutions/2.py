
T = int(input())

for _ in range(T):
    N = int(input())

    cell = [list(map(int, list(input()))) for _ in range(N)]

    def dfs(x, y):

        if x < 0 or y < 0:
            return

        if cell[y][x] == 0:
            return

        cell[y][x] = 0
        dfs(x, y - 1)
        dfs(x - 1, y)

    for x in range(N):
        dfs(x, N - 1)

    for y in range(N):
        dfs(N - 1, y)

    for c in cell:
        if max(c) == 1:
            print("NO")
            break
    else:
        print("YES")

