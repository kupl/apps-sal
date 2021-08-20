from math import sqrt
for x in range(int(input())):
    N = int(input())
    sum = N * (N + 1) // 2
    if sum % 2 != 0:
        print(0)
    else:
        m = int(sqrt(1 + 4 * sum) - 1) // 2
        if m * (m + 1) // 2 == sum // 2:
            print((m - 1) * m // 2 + N - m + (N - m - 1) * (N - m) // 2)
        else:
            print(N - m)
