# cook your dish here
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
    count = 1
    for j in range(D + 1, C):
        list1[0][j] = list1[0][j] - count
        count += 1
if D + 1 < R:
    count = 1
    for i in range(D + 1, R):
        list1[i][0] = list1[i][0] - count
        count += 1
list2 = copy.deepcopy(list1)
for j in range(1, R):
    for i in range(1, C):
        if list2[j][i] != 0:
            list2[j][i] = list2[j - 1][i] + list2[j][i - 1]
answer = (list2[R - 1][C - 1]) % MOD
# for i in range(len(list1)):
# print(list1[i])
# print()
# for j in range(len(list2)):
# print(list2[j])
print(answer)
