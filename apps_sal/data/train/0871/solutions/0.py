import sys

t = int(input())
# print(t)
for _ in range(t):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input())
    ans = []
    for i in range(n):
        ans.append([])
        for j in range(m):
            ans[i].append([])
    for i in range(n):
        for j in range(m):
            c = 0
            if s[i][j] == 'U':
                for k in range(i, -1, -1):
                    if s[k][j] == '#':
                        break
                    ans[k][j].append(c)
                    c += 1
            elif s[i][j] == 'D':
                for k in range(i, n):
                    if s[k][j] == '#':
                        break
                    ans[k][j].append(c)
                    c += 1
            elif s[i][j] == 'L':
                for k in range(j, -1, -1):
                    if s[i][k] == '#':
                        break
                    ans[i][k].append(c)
                    c += 1
            elif s[i][j] == 'R':
                for k in range(j, m):
                    if s[i][k] == '#':
                        break
                    ans[i][k].append(c)
                    c += 1
    for i in range(n):
        for j in range(m):
            ans[i][j].sort()
    res = []
    for i in range(n):
        for j in range(m):
            c = 1
            # print(ans[i][j])
            for k in range(1, len(ans[i][j])):
                # print(ans[i][j][k])
                if ans[i][j][k] == ans[i][j][k - 1]:
                    c += 1
                else:
                    if c != 1:
                        res.append(c)
                    c = 1
                if k == len(ans[i][j]) - 1:
                    if c != 1:
                        res.append(c)
    pairs = 0
    # print(res)
    for i in range(len(res)):
        pairs += ((res[i] * (res[i] - 1)) // 2)

    print(pairs)
