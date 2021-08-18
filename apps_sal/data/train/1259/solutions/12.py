def prettynumber(m, n):
    count = 0
    for i in range(m, n + 1):
        x = i % 10
        if (x == 2 or x == 3 or x == 9):
            count += 1
    print(count)


def __starting_point():
    for j in range(int(input())):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])
        prettynumber(a, b)


__starting_point()
