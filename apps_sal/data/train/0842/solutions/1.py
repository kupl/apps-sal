try:
    t = int(input())
    for a in range(t):
        k = int(input())
        x = 0
        y = k - 1
        n = 1
        for i in range(k):
            for j in range(k):
                if (j == x or j == y):
                    print(n, end="")
                else:
                    print(" ", end="")
            x += 1
            y -= 1
            n += 1
            print()
except EOFError:
    pass
