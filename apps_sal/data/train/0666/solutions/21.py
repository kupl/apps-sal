try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = 1
        for i in range(n):
            for j in range(n):
                print(c, end='')
                c += 1
            print()
except EOFError:
    pass
