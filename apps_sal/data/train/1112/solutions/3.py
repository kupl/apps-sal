t = int(input())
for _ in range(t):
    n = int(input())
    k = (n * (n + 1)) / 2

    t = 1
    for i in range(n):
        for j in range(n - i):
            print(t, end="")
            t += 1
        print()
