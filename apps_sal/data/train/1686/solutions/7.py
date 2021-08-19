(R, C, d) = map(int, input().split())
table = []
for i in range(R):
    temp = list(map(int, input().split()))
    table.append(temp)
if R >= C:
    temp1 = R
else:
    temp1 = C
for i in range(d + 1, temp1):
    try:
        table[0][i] = 0
        table[i][0] = 0
    except:
        try:
            table[i][0] = 0
        except:
            continue
for i in range(C):
    if table[0][i] == 0:
        for j in range(i, C):
            table[0][j] = 0
        break
for i in range(R):
    if table[i][0] == 0:
        for j in range(i, R):
            table[j][0] = 0
        break
answer = table.copy()
for i in range(1, R):
    for j in range(1, C):
        if answer[i][j] != 0:
            answer[i][j] = answer[i - 1][j] + answer[i][j - 1]
print(str(answer[R - 1][C - 1] % 20011))
