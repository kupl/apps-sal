import copy
MOD = 20011
R, C, D = map(int, input().split())
list1 = []
for i in range(R):
    temp = list(map(int, input().split()))
    list1.append(temp)
for j in range(C):
    if list1[0][j] == 0 or j > D:
        for i in range(j, C):
            list1[0][i] = 0
        break
for i in range(R):
    if list1[i][0] == 0 or i > D:
        for j in range(i, R):
            list1[j][0] = 0
        break
list2 = copy.deepcopy(list1)
for j in range(1, R):
    for i in range(1, C):
        if list2[j][i] != 0:
            list2[j][i] = list2[j - 1][i] + list2[j][i - 1]
answer = (list2[R - 1][C - 1]) % MOD
print(answer)
