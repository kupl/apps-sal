from math import inf
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    a = [[0] * (m+2) for _ in range(n+2)]
    for i in range(n):
        s = input()
        for j, x in enumerate(s):
            a[i][j] = x
    r -= 1
    c -= 1
    ans = [[[inf, inf, inf] for i in range(m)] for j in range(n)]
    ans[r][c][0] = 0
    touched = set()
    touched.add((r, c, 0))
    while len(touched):
        visited = set()
        while len(touched):
            r, c, o = touched.pop()
            count = 1 + ans[r][c][o]
            if o == 0:
                if a[r][c+1] == '1' and a[r][c+2] == '1' and ans[r][c+1][1] > count:
                    ans[r][c+1][1] = count
                    visited.add((r, c+1, 1))
                if a[r][c-2] == '1' and a[r][c-1] == '1' and ans[r][c-2][1] > count:
                    ans[r][c-2][1] = count
                    visited.add((r, c-2, 1))
                if a[r+1][c] == '1' and a[r+2][c] == '1' and ans[r+1][c][2] > count:
                    ans[r+1][c][2] = count
                    visited.add((r+1, c, 2))
                if a[r-1][c] == '1' and a[r-2][c] == '1' and ans[r-2][c][2] > count:
                    ans[r-2][c][2] = count
                    visited.add((r-2, c, 2))
            elif o == 1:
                if a[r][c+2] == '1' and ans[r][c+2][0] > count:
                    ans[r][c+2][0] = count
                    visited.add((r, c+2, 0))
                if a[r][c-1] == '1' and ans[r][c-1][0] > count:
                    ans[r][c-1][0] = count
                    visited.add((r, c-1, 0))
                if a[r+1][c] == '1' and a[r+1][c+1] == '1' and ans[r+1][c][1] > count:
                    ans[r+1][c][1] = count
                    visited.add((r+1, c, 1))
                if a[r-1][c] == '1' and a[r-1][c+1] == '1' and ans[r-1][c][1] > count:
                    ans[r-1][c][1] = count
                    visited.add((r-1, c, 1))
            else:
                if a[r][c+1] == '1' and a[r+1][c+1] == '1' and ans[r][c+1][2] > count:
                    ans[r][c+1][2] = count
                    visited.add((r, c+1, 2))
                if a[r][c-1] == '1' and a[r+1][c-1] == '1' and ans[r][c-1][2] > count:
                    ans[r][c-1][2] = count
                    visited.add((r, c-1, 2))
                if a[r+2][c] == '1' and ans[r+2][c][0] > count:
                    ans[r+2][c][0] = count
                    visited.add((r+2, c, 0))
                if a[r-1][c] == '1' and ans[r-1][c][0] > count:
                    ans[r-1][c][0] = count
                    visited.add((r-1, c, 0))
        touched = visited
    for i in range(n):
        for j in range(m):
            print(ans [i][j][0] if ans[i][j][0] != inf else -1, end=' ')
        print()
