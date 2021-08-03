def EXEC(n):
    if n < 3:
        return n
    else:
        x, y = 1, 2
        for _ in range(2, n):
            z = (x + y) % 15746
            x, y = y, z
        return y % 15746


print(EXEC(int(input())))
