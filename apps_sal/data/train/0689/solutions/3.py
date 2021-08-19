t = int(input())
a = list()
for _ in range(t):
    a.append(list(map(int, input().split())))
count = 0
for i in range(t):
    for j in range(i + 1, t):
        if a[i][1] + a[j][1] == 0:
            count += 1
            print('YES')
            break
    if count != 0:
        break
if count == 0:
    print('NO')
