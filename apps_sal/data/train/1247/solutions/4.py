import sys
sys.setrecursionlimit(10000000)


def mergeSortInversions(arr):
    if len(arr) == 1:
        return (arr, 0)
    larr = len(arr)
    (a, b) = (arr[:larr // 2], arr[larr // 2:])
    (a, ai) = mergeSortInversions(a)
    (b, bi) = mergeSortInversions(b)
    (c, i, j) = ([], 0, 0)
    inversions = 0 + ai + bi
    la = len(a)
    while i < la and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            (j, inversions) = (j + 1, inversions + (la - i))
    c += a[i:] + b[j:]
    return (c, inversions)


for _ in range(int(input())):
    (n, d) = map(int, input().split())
    p = [int(o) for o in input().split()]
    (array, flag, ans, dumarr) = ([[] for i in range(d)], 0, 0, [0] * n)
    for i in range(n):
        array[i % d].append(p[i])
        if p[i] % (i % d + 1) != 0:
            flag = 1
    for i in range(d):
        (array[i], v) = mergeSortInversions(array[i])
        for j in range(len(array[i])):
            dumarr[i + j * d] = array[i][j]
        ans += v
    print(ans) if dumarr == sorted(p) else print(-1)
