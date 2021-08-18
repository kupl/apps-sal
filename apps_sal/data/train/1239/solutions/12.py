t = int(input())
while(t):
    n = int(input())
    for i in range(n, -1, -1):
        for j in range(n, i - 1, -1):
            print(j, end="")
        print()
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(j, end="")
        print()
    t -= 1
