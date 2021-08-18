def subCount(arr, n, k):

    mod = []
    for i in range(k + 1):
        mod.append(0)

    cumSum = 0
    for i in range(n):
        cumSum = cumSum + arr[i]

        mod[((cumSum % k) + k) % k] = mod[((cumSum % k) + k) % k] + 1

    result = 0

    for i in range(k):

        if (mod[i] > 1):
            result = result + (mod[i] * (mod[i] - 1)) // 2

    result = result + mod[0]

    return result


for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = []
    for i in range(len(a)):
        b.append(int(a[i][0]))
    print(subCount(b, len(b), 10))
