for _ in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        for j in range(1, i):
            print("*", end="")
        for j in range(n - i + 1, 0, -1):
            print(j, end="")

        print()
