def swap(i, j):
    (arr[i], arr[j]) = (arr[j], arr[i])


def inversion(li):
    n = len(li)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if li[j] < li[i]:
                inversions += 1
    return inversions


def right_shift(i):
    (arr[i], arr[i + 1], arr[i + 2]) = [arr[i + 2], arr[i], arr[i + 1]]


t = int(input())
for you in range(t):
    n = int(input())
    l = input().split()
    arr = [int(i) for i in l]
    arr1 = list(arr)
    lfi = []
    lo = []
    for i in range(n):
        lo.append((arr[i], i))
    lo.sort()
    hashi = dict()
    for i in range(n):
        hashi[lo[i][1]] = i + 1
    arr = []
    for i in range(n):
        arr.append(hashi[i])
    poss = 1
    if inversion(arr) % 2:
        for i in range(n):
            for j in range(i + 1, n):
                if arr1[i] == arr1[j]:
                    swap(i, j)
                    poss = 0
                    break
            if poss == 0:
                break
    z = list(arr)
    z.sort()
    for j in range(n):
        for i in range(n - 2 - j):
            maxa = max(arr[i], arr[i + 1], arr[i + 2])
            if maxa == arr[i + 2]:
                continue
            elif maxa == arr[i + 1]:
                lfi.append(i)
                right_shift(i)
            else:
                lfi.append(i)
                lfi.append(i)
                right_shift(i)
                right_shift(i)
    if arr == z:
        print(len(lfi))
        for i in lfi:
            print(i + 1, end=' ')
        print()
    else:
        print(-1)
