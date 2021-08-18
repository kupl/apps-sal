
import sys
import math
import copy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"


def main():
    q = int(input())
    for i in range(q):
        print((wc()))


def wc():
    a, b = list(map(int, input().split()))
    if a == b:
        return 2 * (a - 1)
    if b > a:
        a, b = b, a
    sqt = (a * b) ** 0.5
    area1 = math.ceil(sqt) - 1
    area2 = math.ceil(sqt) - 1 - b
    area3 = b - 1
    adj = -1 if (math.ceil(sqt) - 1) * math.ceil(sqt) >= a * b else 0
    return area1 + area2 + area3 + adj


main()
