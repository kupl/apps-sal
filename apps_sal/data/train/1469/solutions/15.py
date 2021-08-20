try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = 2
        for i in range(n):
            z = c
            for j in range(n):
                print(z, end='')
                z += 1
            c += 1
            print()
except EOFError:
    pass
