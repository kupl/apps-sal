import math

t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    if n <= 3:
        print(1)
        print(n, end=" ")
        for i in range(1, n + 1):
            print(str(i), end=" ")
        print()
    else:
        print(math.ceil((n - 3) / 2) + 1)
        a = ["3 1 2 3"]
        for i in range(4, n, 2):
            a.append("2 " + str(i) + " " + str(i + 1))
        if (n & 1) == 0:
            a.append("1 " + str(n))
        print(*a, sep="\n")
