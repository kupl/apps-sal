from math import inf


def solve():
    (n, m, a, b) = map(int, input().split())
    grid = [[0] * m for i in range(n)]
    (row_cnt, col_cnt) = ([0] * n, [0] * m)
    for i in range(n):
        for cnt in range(a):
            mini = inf
            ind = None
            for j in range(m):
                if col_cnt[j] < mini:
                    mini = col_cnt[j]
                    ind = j
            grid[i][ind] = 1
            row_cnt[i] += 1
            col_cnt[ind] += 1
    if all((r == a for r in row_cnt)) and all((c == b for c in col_cnt)):
        print('YES')
        for row in grid:
            print(''.join(list(map(str, row))))
    else:
        print('NO')


def main():
    for _ in range(int(input())):
        solve()


main()
