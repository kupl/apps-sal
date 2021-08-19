try:

    def um(a, r, x):
        z = [[0 for i in range(a + 1)] for i in range(x + 1)]
        for i in range(x + 1):
            for j in range(a + 1):
                if j == 0:
                    z[i][j] = 1
                elif i == 0:
                    z[i][j] = 0
                elif r[i - 1] <= j:
                    z[i][j] = z[i - 1][j - r[i - 1]] + z[i - 1][j]
                else:
                    z[i][j] = z[i - 1][j]
        return z[x][a]
    for _ in range(int(input())):
        b = int(input())
        a = int(input())
        r = [int(i) for i in input().split()]
        x = len(r)
        print(um(a, r, x))
except EOFError as y:
    pass
