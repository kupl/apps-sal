#!/usr/bin/python3
import math


def xor_solution(l, r):
    sum_xors = 0
    for i in range(l, r + 1):
        if((i & (i - 1)) == 0):
            sum_xors = sum_xors - 1
        else:
            sum_xors = sum_xors + (i & (i - 1))
    return sum_xors


def sum_xor(x):
    if(x == 0):
        return 0
    sum_n = (x * (x + 1)) // 2
    temp = x
    power2 = 1
    sum_a = 0
    while(x >= 1):
        count = (x + 1) // 2
        sum_a += count * power2
        x = x - count
        power2 = power2 * 2

    sum_b = sum_n - sum_a
    return (sum_b - (int(math.log2(temp)) + 1))


def main():
    test_case = int(input())
    ans = []
    while(test_case > 0):
        l, r = list(map(int, input().split()))
        ans.append(sum_xor(r) - sum_xor(l - 1))

        test_case -= 1

    for i in ans:
        print(i)


def __starting_point():
    main()


__starting_point()
