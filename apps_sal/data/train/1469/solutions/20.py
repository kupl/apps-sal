for _ in range(int(input())):
    n = int(input())
    c = 1
    for i in range(2, n + 2):
        for j in range(0, n):
            print(i + j, end="")
            c += 2
        print()
