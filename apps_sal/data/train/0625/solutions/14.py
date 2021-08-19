t = int(input())


def subCount(arr, n, k):
    mod = []
    for i in range(k + 1):
        mod.append(0)
    allSum = 0
    for i in range(n):
        allSum = allSum + arr[i]
        mod[allSum % k] += 1
    res = 0
    for i in range(k):
        if mod[i] > 1:
            res = res + mod[i] * (mod[i] - 1) // 2
    res = res + mod[0]
    return res


for _ in range(t):
    n = int(input())
    a = [int(k) // 10 ** 8 for k in input().split()]
    print(subCount(a, n, 10))
