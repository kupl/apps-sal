import itertools
import numpy as np
b = np.zeros((100001), dtype=np.int)


def power2(a):
    b[0] = 1
    if b[a] > 0:
        return b[a]
    else:
        for i in range(1, a + 1):

            b[i] = b[i - 1] * 2
            if b[i] > (10**9 + 7):
                b[i] = b[i] % (10**9 + 7)
        return b[a]


def __starting_point():
    t = eval(input())
    for i in range(t):
        s = input()
        n = eval(input())
        f_list = []
        count = 0
        for j in range(n):
            f_list.append(input())
        inp = ""
        bin_list = []
        for j in range(len(s)):
            if s[j] == 'w':
                inp = inp + '0'
            else:
                inp = inp + '1'
        # print inp

        a = np.zeros((1024), dtype=np.int)
        for j in range(n):
            s1 = ""
            for k in range(len(f_list[j])):
                if f_list[j][k] == '+':
                    s1 = s1 + '1'
                else:
                    s1 = s1 + '0'
            if n < 1024:
                bin_list.append(s1)
            p = int(s1, 2)
            if a[p] == 0:
                count = count + 1
            a[p] = a[p] + 1
        count_2 = 0

        # print a

        if n < 1024:
            dp = np.zeros((n + 1, 1024), dtype=np.int64)
            dp[0, 0] = 1
            for j in range(1, n + 1):
                for k in range(1024):
                    # print j-1
                    # print k^int(bin_list[j-1],2)

                    dp[j, k] = (dp[j - 1][k] + dp[j - 1][k ^ int(bin_list[j - 1], 2)]) % (10**9 + 7)

                # print dp
            p = 1023 ^ int(inp, 2)

            print(dp[n, p] % (10**9 + 7))

        else:

            dp = np.zeros((1025, 1024), dtype=np.int64)
            dp[0, 0] = 1
            for j in range(1, 1025):
                count_2 = count_2 + 1
                if a[j - 1] > 0:
                    l = power2(a[j - 1] - 1)
                for k in range(1024):
                    # print j-1
                    # print k^int(bin_list[j-1],2)
                    if a[j - 1] > 0:
                        dp[j, k] = (((dp[j - 1][k] + dp[j - 1][k ^ (j - 1)]) % (10**9 + 7)) * l) % (10**9 + 7)
                    elif dp[j - 1][k] > 0:
                        dp[j, k] = dp[j - 1][k]

                if count_2 == count:
                    break
                # print dp
            p = 1023 ^ int(inp, 2)

            print(dp[j, p] % (10**9 + 7))


__starting_point()
