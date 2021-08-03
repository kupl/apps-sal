x = int(input())
for i in range(x):
    n = int(input())
    p = 1
    for j in range(n):
        for k in range(n - j):
            print(p, end="")
            p += 1
        print()
