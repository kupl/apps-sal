def subCount(arr, n, k):
    mod = []
    for i in range(k + 1):
        mod.append(0)
    cumSum = 0
    for i in range(n):
        cumSum = cumSum + arr[i]
        mod[(cumSum % k + k) % k] = mod[(cumSum % k + k) % k] + 1
    result = 0
    for i in range(k):
        if mod[i] > 1:
            result = result + mod[i] * (mod[i] - 1) // 2
    result = result + mod[0]
    return result


for _ in range(int(input())):
    n = int(input())
    ar = [int(i) for i in input().split()]
    a = []
    for i in ar:
        if i == 100000000:
            a.append(1)
        else:
            a.append(9)
    print(subCount(a, n, 10))
