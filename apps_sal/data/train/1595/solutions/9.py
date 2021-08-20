import itertools
import numpy as np


def power2(a):
    sum_1 = 1
    for i in range(1, a + 1):
        sum_1 = sum_1 * 2
        if sum_1 > 10 ** 9 + 7:
            sum_1 = sum_1 % (10 ** 9 + 7)
    return sum_1


def __starting_point():
    t = eval(input())
    for i in range(t):
        s = input()
        n = eval(input())
        f_list = []
        for j in range(n):
            f_list.append(input())
        inp = ''
        bin_list = []
        for j in range(len(s)):
            if s[j] == 'w':
                inp = inp + '0'
            else:
                inp = inp + '1'
        a = np.zeros(1024, dtype=np.int)
        for j in range(n):
            s1 = ''
            for k in range(len(f_list[j])):
                if f_list[j][k] == '+':
                    s1 = s1 + '1'
                else:
                    s1 = s1 + '0'
            if n < 1024:
                bin_list.append(s1)
            p = int(s1, 2)
            a[p] = a[p] + 1
        if n < 1024:
            dp = np.zeros((n + 1, 1024), dtype=np.int)
            dp[0, 0] = 1
            for j in range(1, n + 1):
                for k in range(1024):
                    dp[j, k] = (dp[j - 1][k] + dp[j - 1][k ^ int(bin_list[j - 1], 2)]) % (10 ** 9 + 7)
            p = 1023 ^ int(inp, 2)
            print(dp[n, p] % (10 ** 9 + 7))
        else:
            dp = np.zeros((1025, 1024), dtype=np.int)
            dp[0, 0] = 1
            for j in range(1, 1025):
                for k in range(1024):
                    if a[j - 1] > 0:
                        dp[j, k] = (dp[j - 1][k] + dp[j - 1][k ^ j - 1]) % (10 ** 9 + 7) * power2(a[j - 1] - 1) % (10 ** 9 + 7)
                    elif dp[j - 1][k] > 0:
                        dp[j, k] = dp[j - 1][k]
            p = 1023 ^ int(inp, 2)
            print(dp[1024, p] % (10 ** 9 + 7))


__starting_point()
