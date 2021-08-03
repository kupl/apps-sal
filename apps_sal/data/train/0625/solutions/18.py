def subCount(arr, n, k, mod, cumSum, result):
    for i in range(k + 1):
        mod.append(0)
    for i in range(n):
        cumSum += arr[i]
        mod[((cumSum % k) + k) % k] = mod[((cumSum % k) + k) % k] + 1
    for i in range(k):
        if (mod[i] > 1):
            result = result + (mod[i] * (mod[i] - 1)) // 2
    return result + mod[0]


for _ in range(int(input())):
    n, a = int(input()), list(map(int, input().split()))
    for i in range(n):
        a[i] //= (10**8)
    print(subCount(a, n, 10, [], 0, 0))
