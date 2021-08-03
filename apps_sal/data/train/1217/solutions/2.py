from sys import stdin

mod = 10**9 + 7
max_val = 135

cache2 = [[0] * max_val for _ in range(max_val)]
done = [[False] * max_val for _ in range(max_val)]


def f2(x, y):
    if done[x][y]:
        res = cache2[x][y]
    elif x == 0 or y == 0:
        res = 1
        cache2[x][y] = res
        done[x][y] = True
    elif x > y:
        res = f2(y, y)
        cache2[x][y] = res
        done[x][y] = True
    else:
        res = sum(f2(y - i, i) for i in range(x + 1))
        cache2[x][y] = res
        done[x][y] = True
    return res % mod


def solve():
    n = int(stdin.readline().strip())
    a = list(map(int, stdin.readline().strip().split()))

    cache = [[[0] * max_val for _ in range(max_val)] for _ in range(51)]
    done = [[[False] * max_val for _ in range(max_val)] for _ in range(51)]

    def f(i, x, y):
        if done[i][x][y]:
            res = cache[i][x][y]
        elif i == n - 1:
            res = 1
            cache[i][x][y] = res
            done[i][x][y] = True
        elif i == n - 2:
            res = f2(x, y)
            cache[i][x][y] = res
            done[i][x][y] = True
        elif x == 0:
            res = f(i + 1, y, a[i + 2])
            cache[i][x][y] = res
            done[i][x][y] = True
        else:
            k = min(x, y)
            res = 0
            for z in range(k + 1):
                res += f(i + 1, y - z, a[i + 2] + z)
                res %= mod
            cache[i][x][y] = res
            done[i][x][y] = True
        return res % mod

    print(f(0, a[0], a[1]) if n >= 2 else 1)


t = int(stdin.readline().strip())
for _ in range(t):
    solve()
