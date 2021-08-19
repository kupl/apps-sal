"""
    Author - Subhajit Das
    University of Engineering and Management, Kolkata
    04/07/2019
"""


def main():
    for _ in range(int(input())):
        (n, m, k) = list(map(int, input().split()))
        field = [[0] * m for _ in range(n)]
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ans = 0
        while k != 0:
            (r, c) = list(map(int, input().split()))
            r -= 1
            c -= 1
            field[r][c] = 1
            for (dx, dy) in moves:
                (nr, nc) = (r + dx, c + dy)
                if nr < 0 or nr >= n or nc < 0 or (nc >= m):
                    ans += 1
                    continue
                if field[nr][nc] == 1:
                    ans -= 1
                else:
                    ans += 1
            k -= 1
        print(ans)


def __starting_point():
    main()


__starting_point()
