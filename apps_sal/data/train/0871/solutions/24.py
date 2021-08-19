t = int(input())
for _ in range(t):
    r, c = map(int, input().split())
    a = [list(input()) for _ in range(r)]
    ans = 0
    for i, row in enumerate(a):
        for j, x in enumerate(row):
            if x == 'R':
                for k, y in enumerate(row[j + 1:]):
                    if y == '#':
                        break
                    if k % 2 and y == 'L':
                        ans += 1
            elif x in 'UD':
                b = a[i + 1:] if x == 'D' else reversed(a[:i])
                for k, row1 in enumerate(b, 1):
                    if row1[j] == '#':
                        break
                    if k % 2 == 0 and row1[j] == 'UD'[x == 'U']:
                        ans += 1
                    m = j - k
                    if m >= 0 and row1[m] == 'R' and '#' not in row1[m + 1: j]:
                        ans += 1
                    m = j + k
                    if m < c and row1[m] == 'L' and '#' not in row1[j + 1: m]:
                        ans += 1
                a[i][j] = None
    print(ans)
