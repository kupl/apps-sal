import sys


def findRoom(x, y, i):
    R = [(x, y)]
    GRID[x][y] = i
    for n in R:
        GRID[n[0]][n[1]] = i
        if n[0] > 0 and GRID[n[0] - 1][n[1]] == 0 and H[n[0] - 1][n[1]]:
            GRID[n[0] - 1][n[1]] = i
            R.append((n[0] - 1, n[1]))
        if n[0] < N - 1 and GRID[n[0] + 1][n[1]] == 0 and H[n[0]][n[1]]:
            GRID[n[0] + 1][n[1]] = i
            R.append((n[0] + 1, n[1]))
        if n[1] > 0 and GRID[n[0]][n[1] - 1] == 0 and V[n[0]][n[1] - 1]:
            GRID[n[0]][n[1] - 1] = i
            R.append((n[0], n[1] - 1))
        if n[1] < M - 1 and GRID[n[0]][n[1] + 1] == 0 and V[n[0]][n[1]]:
            GRID[n[0]][n[1] + 1] = i
            R.append((n[0], n[1] + 1))


def roomPrice(r):
    wall_price_0 = wall_price_1 = 0
    for i in range(R):
        if C[i][r] and T[i] != 1:
            wall_price_0 += C[i][r] * K
        else:
            wall_price_1 += C[i][r] * K
    return [wall_price_0 + Rooms[r][0], wall_price_1 + Rooms[r][1]]


def total_price():
    price = 0
    for r in range(R):
        for i in range(r):
            if C[i][r] and T[i] != T[r]:
                price += C[i][r] * K
                price += Rooms[r][T[r] - 1]
    return price


def solve(r):
    if r == R:
        return 0
    wall_price_0 = 0
    wall_price_1 = 0
    for i in range(r):
        if C[i][r] and T[i] != 1:
            wall_price_0 += C[i][r] * K
        else:
            wall_price_1 += C[i][r] * K
    if T[r] != 0:
        return [wall_price_0, wall_price_1][T[r] - 1] + Rooms[r][T[r] - 1] + solve(r + 1)
    T[r] = 1
    result = solve(r + 1) + wall_price_0 + Rooms[r][0]
    T[r] = 2
    result = min(solve(r + 1) + wall_price_1 + Rooms[r][1], result)
    T[r] = 0
    return result


f = sys.stdin
(N, M, W, K, R) = list(map(int, f.readline().split(' ')))
T = [0] * R
GRID = list(map(list, [[0] * M] * N))
H = list(map(list, [[1] * M] * N))
V = list(map(list, [[1] * M] * N))
Walls = []
for _ in range(W):
    (x0, y0, x1, y1) = list(map(int, f.readline().split(' ')))
    x0 -= 1
    x1 -= 1
    y0 -= 1
    y1 -= 1
    if x0 == x1:
        V[x0][y0] = 0
    else:
        H[x0][y0] = 0
    Walls.append([x0, y0, x1, y1])
Rooms = []
for i in range(R):
    (x, y, t1, t2) = list(map(int, f.readline().split(' ')))
    findRoom(x - 1, y - 1, i + 1)
    Rooms.append([t1, t2])
C = list(map(list, [[0] * R] * R))
for w in Walls:
    r1 = GRID[w[0]][w[1]] - 1
    r2 = GRID[w[2]][w[3]] - 1
    C[r1][r2] += 1
    C[r2][r1] += 1
Stable = [False] * R
for r in range(R):
    walls_max_price = sum(C[r]) * K
    if walls_max_price <= abs(Rooms[r][0] - Rooms[r][1]):
        T[r] = 1 + (Rooms[r][0] > Rooms[r][1])
        Stable[r] = True


def try_teams():
    for r in range(R):
        if not Stable[r]:
            T[r] = 1 + (r & 1)
        change = True
    while change:
        change = False
        for r in range(R):
            price = roomPrice(r)
            if price[T[r] - 1] > price[2 - T[r]]:
                T[r] = 3 - T[r]
                change = True
    print(total_price())


print(solve(0))
