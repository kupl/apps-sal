import numpy as np
t = int(input())
arr = []
for i in range(t):
    inp = input()
    arr.append(list(map(int, inp.split(' '))))


def gen_array(arr1, arr2, mp, rn):
    arrg = []
    if len(arr1) != len(arr2):
        arr1.append(0)
    for j in range(len(arr2) - 1):
        arrg.append(arr1[0] * arr2[j + 1] - arr2[0] * arr1[j + 1])
    ctz = not np.any(arrg)
    if ctz == True:
        for j in range(len(arrg)):
            arrg[j] = (mp + 4 - rn - 2 * (j + 1)) * arr1[j]
    return arrg


def check(rht):
    for i in range(len(rht) - 1):
        if rht[i][0] * rht[i + 1][0] <= 0:
            print(0)
            break
    else:
        print(1)


rh = []
for i in range(t):
    rh.append([])
    arr1 = []
    arr2 = []
    for j in range(len(arr[i]) - 1, -1, -1):
        if j % 2 == 0:
            arr1.append(arr[i][j])
        else:
            arr2.append(arr[i][j])
    arr1.reverse()
    arr2.reverse()
    rh[i].append(arr1)
    rh[i].append(arr2)
    for j in range(2, len(arr[i])):
        rh[i].append(gen_array(rh[i][j - 1], rh[i][j - 2], arr[i][0], j + 1))
    check(rh[i])
