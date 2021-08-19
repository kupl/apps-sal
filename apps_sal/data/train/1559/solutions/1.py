import sys
L = 10 ** 9 + 7


def mat_mult(lst1, lst2, r, c, m):
    res = [[0] * m for i in range(r)]
    for i in range(r):
        for j in range(m):
            res[i][j] = 0
            for k in range(c):
                res[i][j] = (res[i][j] + lst1[i][k] * lst2[k][j]) % L
    return res


def main():
    mat = [[-1, 0, 0, 0], [1, 3, 0, 0], [0, 0, -1, 0], [0, 0, 1, 3]]
    result = [[24, 108, 12, 36]]
    t = int(input())
    lst = [None] * t
    for i in range(t):
        lst[i] = int(input())
    for i in range(t):
        if lst[i] == 1:
            print(4)
            continue
        if lst[i] == 2:
            print(12)
            continue
        if lst[i] == 3:
            print(24)
            continue
        mat = [[-1, 0, 0, 0], [1, 3, 0, 0], [0, 0, -1, 0], [0, 0, 1, 3]]
        result = [[24, 108, 12, 36]]
        N = lst[i] - 3
        while N > 0:
            if N % 2 == 0:
                mat = mat_mult(mat, mat, 4, 4, 4)
                N = N / 2
            if N % 2 == 1:
                result = mat_mult(result, mat, 1, 4, 4)
                N = N - 1
        print(result[0][0])


def __starting_point():
    main()


__starting_point()
