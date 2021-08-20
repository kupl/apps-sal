import sys
sys.setrecursionlimit(10 ** 6)


def int1(x):
    return int(x) - 1


def p2D(x):
    return print(*x, sep='\n')


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


def main():
    (k, n) = MI()
    end = n - 1
    if k % 2:
        ans = [k // 2 + 1] * n
        for _ in range(n // 2):
            if ans[end] == 1:
                end -= 1
            else:
                ans[end] -= 1
                if end != n - 1:
                    for i in range(end + 1, n):
                        ans[i] = k
                    end = n - 1
    else:
        ans = [k // 2] + [k] * (n - 1)
    print(*ans[:end + 1])


main()
