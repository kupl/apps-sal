# cook your dish here
inputs = list(map(int, input().split()))
N = inputs[0]
M = inputs[1]
W = inputs[2]
B = inputs[3]
list1 = [["."] * M for i in range(N)]
for i in range(4, (2 * W) + 4, 2):
    list1[inputs[i] - 1][inputs[i + 1] - 1] = 'W'
for j in range((2 * W) + 4, len(inputs), 2):
    list1[inputs[j] - 1][inputs[j + 1] - 1] = "B"
list2 = [[0] * M for i in range(N)]
first = 0
distance = 0
whites = 0
js = 0
for i in range(N):
    first = 0
    for j in range(M):
        if list1[i][j] == "." and first == 0:
            whites = 0
            first = 1
            distance = 1
            for k in range(j + 1, M):
                if list1[i][k] == "B":
                    distance += 1
                    first = 0
                    break
                elif list1[i][k] == "W":
                    whites += 1
                    distance += 1
                    if whites > 1:
                        first = 0
                        whites = 0
                        break
                elif list1[i][k] == ".":
                    distance += 1
            js = j + 1
            js -= 1
            list2[i][j] = distance + 0
        elif list1[i][j] == ".":
            list2[i][j] = list2[i][js] - (j - js)
        else:
            list2[i][j] = 0
    first = 0
# for row in list2:
    # print(row)
total = 0
for i in range(N):
    for j in range(M):
        total += list2[i][j]
print(total)
