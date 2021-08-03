testcases = int(input())
for i in range(testcases):
    n = int(input())
    n -= 1
    sum1 = n * (n + 1) * (2 * n + 1) // 6
    print(sum1)
