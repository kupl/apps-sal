for _ in range(int(input())):
    n = int(input())
    r = 1
    t = n + 1
    for i in range(n):
        t -= 1
        for j in range(t, 0, -1):
            print(r, end="")
            r += 1
        print()
