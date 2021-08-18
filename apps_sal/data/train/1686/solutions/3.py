import copy
MOD = 20011
R, C, D = map(int, input().split())
list1 = []
for i in range(R):
    temp = list(map(int, input().split()))
    list1.append(temp)
for j in range(C):
    if list1[0][j] == 0:
        for i in range(j, C):
            list1[0][i] = 0
        break
for i in range(R):
    if list1[i][0] == 0:
        for j in range(i, R):
            list1[j][0] = 0
        break
if D + 1 < C:
    for j in range(D + 1, C):
        list1[0][j] = 0
if D + 1 < R:
    for i in range(D + 1, R):
        list1[i][0] = 0
list2 = copy.deepcopy(list1)
for j in range(1, R):
    count = [0 for i in range(R)]
    count1 = [0 for j in range(C)]
    for i in range(1, C):
        if list2[j][i] != 0:
            list2[j][i] = list2[j - 1][i] + list2[j][i - 1]
        if j - D - 1 >= 0 and list2[j - 1][i] != 0:
            list2[j][i] -= list2[j - D - 1][i]
            if j - D - 2 >= 0:
                list2[j][i] += list2[j - D - 2][i]
        if i - D - 1 >= 0 and list2[j][i - 1] != 0:
            list2[j][i] -= list2[j][i - D - 1]
            if i - D - 2 >= 0:
                list2[j][i] += list2[j][i - D - 2]
        if list2[j][i] < 0:
            list2[j][i] = 0
answer = (list2[R - 1][C - 1]) % MOD
print(answer)
