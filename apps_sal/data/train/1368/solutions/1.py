from math import gcd, sqrt, ceil
import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def get_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_list_string():
    return list(map(str, sys.stdin.readline().strip().split()))


def get_string():
    return sys.stdin.readline().strip()


def get_int():
    return int(sys.stdin.readline().strip())


def get_print_int(x):
    sys.stdout.write(str(x) + '\n')


def get_print(x):
    sys.stdout.write(x + '\n')


def solve():
    for _ in range(get_int()):
        (h, x) = get_ints()
        if h >= x:
            get_print('Yes')
        else:
            get_print('No')


solve()
