from math import *


def list_input():
    return list(map(int, input().split()))


def map_input():
    return list(map(int, input().split()))


def map_string():
    return input().split()


def g(n):
    return (n * (n + 1) * (2 * n + 1)) // 6


def f(n):
    ans = 0
    for i in range(1, floor(sqrt(n)) + 1):
        ans += i * (i + floor(n / i)) * (floor(n / i) + 1 - i)
    return ans - g(floor(sqrt(n)))


for _ in range(int(input())):
    n = int(input())
    print(f(n) % 1000000007)
