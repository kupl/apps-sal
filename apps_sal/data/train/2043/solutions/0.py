n = int(input())
arr = []
for i in range(n):
    (l, r) = map(int, input().split())
    arr.append([l, r])
lts = []
for i in range(n):
    if arr[i][0] == 0:
        l = i
        j = i
        while arr[j][1] != 0:
            j = arr[j][1] - 1
        r = j
        lts.append([l, r])
for i in range(1, len(lts)):
    arr[lts[i - 1][1]][1] = lts[i][0] + 1
    arr[lts[i][0]][0] = lts[i - 1][1] + 1
for i in range(n):
    print(arr[i][0], arr[i][1])
