import sys


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    (n, a, b) = input_int_list()
    X = input_int_list()
    dp = [0] * n
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + (X[i] - X[i - 1]) * a, dp[i - 1] + b)
    print(dp[n - 1])
    return


def __starting_point():
    main()


__starting_point()
