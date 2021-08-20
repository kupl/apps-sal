import math


def avg_diags(m):
    diagonal_1 = []
    diagonal_2 = []
    ans1 = 0
    ans2 = 0
    for i in range(len(m)):
        if i % 2 != 0 and m[i][i] >= 0:
            diagonal_1.append(m[i][i])
        if i % 2 == 0 and m[len(m) - 1 - i][i] < 0:
            diagonal_2.append(m[len(m) - 1 - i][i])
    if diagonal_1 == []:
        ans1 = -1
    else:
        ans1 = round(sum(diagonal_1) / len(diagonal_1), 0)
    if diagonal_2 == []:
        ans2 = -1
    else:
        ans2 = round(sum(diagonal_2) * -1 / len(diagonal_2), 0)
    return [ans1, ans2]
