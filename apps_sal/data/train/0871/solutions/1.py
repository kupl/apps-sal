def count_ants(l, r, u, d):
    cnt = 0
    if l is False:
        cnt += 1
    if r is False:
        cnt += 1
    if u is False:
        cnt += 1
    if d is False:
        cnt += 1
    return cnt


def solve(m, row, col):
    ans = 0
    for i in range(row):
        for j in range(col):
            lw = True
            rw = True
            uw = True
            dw = True
            if m[i][j] == '
            continue
            for d in range(1, max(row, col)):
                cnt = 0
                if j - d < 0:
                    lw = False
                if j + d >= col:
                    rw = False
                if i - d < 0:
                    uw = False
                if i + d >= row:
                    dw = False
                if count_ants(lw, rw, uw, dw) > 2:
                    break
                if lw and j - d >= 0:
                    if m[i][j - d] == 'R':
                        cnt += 1
                    elif m[i][j - d] == '
                    lw = False
                if rw and j + d < col:
                    if m[i][j + d] == 'L':
                        cnt += 1
                    elif m[i][j + d] == '
                    rw = False

                if uw and i - d >= 0:
                    if m[i - d][j] == 'D':
                        cnt += 1
                    elif m[i - d][j] == '
                    uw = False

                if dw and i + d < row:
                    if m[i + d][j] == 'U':
                        cnt += 1
                    elif m[i + d][j] == '
                    dw = False
                if cnt > 1:
                    ans += (cnt * (cnt - 1)) // 2
    return ans


def read():
    t = int(input())
    for i in range(t):
        r, c = list(map(int, input().strip().split()))
        m = [[] for i in range(r)]
        for i in range(r):
            s = input().strip()
            m[i] = s
        ans = solve(m, r, c)
        print(ans)


read()
