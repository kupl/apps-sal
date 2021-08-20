def findMax(safePath, relBerries, collectedBerries, cx, cy, n, ans):
    if cx == n - 1 and cy == n - 1:
        ans['reached'] = True
        collectedBerries += relBerries[cx][cy]
        ans['maxberries'] = max(ans['maxberries'], collectedBerries)
    else:
        if collectedBerries <= ans['prev'][cx][cy]:
            return
        else:
            ans['prev'][cx][cy] = collectedBerries
        if cx != n - 1 and safePath[cx + 1][cy] == 1:
            findMax(safePath, relBerries, collectedBerries + relBerries[cx][cy], cx + 1, cy, n, ans)
        if cy != n - 1 and safePath[cx][cy + 1] == 1:
            findMax(safePath, relBerries, collectedBerries + relBerries[cx][cy], cx, cy + 1, n, ans)


(n, m) = map(int, input().split())
relBerries = []
safePaths = []
for i in range(n):
    safePaths.append([0] * n)
for i in range(n):
    relBerries.append(list(map(int, input().split())))
for i in range(m):
    (x, y, s) = map(int, input().split())
    x -= 1
    y -= 1
    for j in range(0, s + 1):
        if x - j >= 0:
            safePaths[x - j][y] = 1
            for z in range(1, s - j + 1):
                if y + z < n:
                    safePaths[x - j][y + z] = 1
                else:
                    break
            for z in range(1, s - j + 1):
                if y - z >= 0:
                    safePaths[x - j][y - z] = 1
                else:
                    break
        if x + j < n and j != 0:
            safePaths[x + j][y] = 1
            for z in range(1, s - j + 1):
                if y + z < n:
                    safePaths[x + j][y + z] = 1
                else:
                    break
            for z in range(1, s - j + 1):
                if y - z >= 0:
                    safePaths[x + j][y - z] = 1
                else:
                    break
ans = {}
ans['maxberries'] = -100000000
ans['reached'] = False
ans['prev'] = []
for i in range(n):
    ans['prev'].append([-100000000] * n)
findMax(safePaths, relBerries, 0, 0, 0, n, ans)
if ans['reached']:
    print('YES')
    print(ans['maxberries'])
else:
    print('NO')
