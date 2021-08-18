
import sys


def IOE():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def dp(a, n):
    mat = [0 for i in range(n)]
    mat[0] = 1
    for i in range(n):
        mat[i] = 1
        for j in range(i):
            if mat[j] != 0 and a[i] % a[j] == 0:
                mat[i] = max(mat[i], mat[j] + 1)
    return max(mat)


def main():
    n = int(sys.stdin.readline())
    a = []
    for _ in range(n):
        a.append(int(sys.stdin.readline()))
    print(dp(a, n))


def __starting_point():
    try:
        IOE()
    except:
        pass
    main()


__starting_point()
