for _ in range(int(input())):
    n = int(input())
    for i in range(n, 0, -1):
        if i % 2 == 0:
            for j in range(n, 0, -1):
                print(j, end="")
            n -= 1
            print("")
        else:
            for j in range(1, n + 1):
                print(j, end="")
            n -= 1
            print("")
