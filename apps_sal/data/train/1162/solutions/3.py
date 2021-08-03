def solve(D):
    c4 = D
    while c4 >= 0:
        if c4 % 7 == 0:
            c7 = D - c4
            if c7 % 4 == 0:
                return c4

        c4 -= 4

    return -1


for _t in range(int(input())):
    print(solve(int(input())))
