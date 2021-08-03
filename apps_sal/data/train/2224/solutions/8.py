n = int(input())
a, b = [*map(int, list(input()))], [*map(int, list(input()))]
changed = [False] * n

for i in range(n):
    if b[i] == 0:
        changed[i] = True

stateCnt = [0] * 4
for i in range(n):
    if a[i] == 1 and changed[i] == True:
        stateCnt[0] += 1
    elif a[i] == 1 and changed[i] == False:
        stateCnt[1] += 1
    elif a[i] == 0 and changed[i] == True:
        stateCnt[2] += 1
    else:
        stateCnt[3] += 1

print(stateCnt[0] * stateCnt[2] + stateCnt[0] * stateCnt[3] + stateCnt[2] * stateCnt[1])
