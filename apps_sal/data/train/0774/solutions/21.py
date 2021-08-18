n, k, p = list(map(int, input().split()))
coor = list(map(int, input().split()))
forw = []
sort_coor = []
for i, each in enumerate(coor):
    sort_coor.append((each, i))
sort_coor.sort()
j = n - 2
msg = {}
max1 = sort_coor[n - 1][0] + k
msg[sort_coor[n - 1][1]] = max1
for i in range(n - 1, 0, -1):
    j = i - 1
    if sort_coor[i][0] - sort_coor[j][0] <= k:
        msg[sort_coor[j][1]] = max1
    else:
        max1 = sort_coor[j][0] + k
        msg[sort_coor[j][1]] = max1

for i in range(p):
    a, b = map(int, input().split())
    if msg[b - 1] == msg[a - 1]:
        print("Yes")
    else:
        print("No")
