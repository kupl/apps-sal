import math
import sys

input = sys.stdin.readline

def main():



    MAX_N = int(1e6) + 1

    dp = [0 for i in range(MAX_N)]
    vals = [[] for i in range(10)]

    for i in range(10):
        dp[i] = i
        vals[i].append(i)


    for i in range(10, MAX_N):
        prod = 1
        for j in str(i):
            if j != '0':
                prod *= int(j)

        dp[i] = dp[prod]
        vals[dp[prod]].append(i)

    q = int(input())

    for i in range(len(vals)):
        vals[i] = sorted(vals[i])

    for i in range(q):
        l,r, k = [int(x) for x in input().split(' ')]
        posl = -1
        posr = -1
        for j in range(25, -1, -1):
            jump = 2**j

            if posl + jump < len(vals[k]) and vals[k][posl+jump] < l:
                posl += jump

            if posr + jump < len(vals[k]) and vals[k][posr+jump] <= r:
                posr += jump

        print(posr - posl)

def __starting_point():
    main()


__starting_point()
