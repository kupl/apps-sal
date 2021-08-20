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
        n = get_int()
        arr = get_list()
        pre = [0] * n
        pre[0] = arr[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + arr[i]
        q = get_int()
        while q:
            (s, e) = get_ints()
            s -= 1
            e -= 1
            if s == 0:
                get_print_int(pre[e])
            else:
                get_print_int(pre[e] - pre[s - 1])
            q -= 1


solve()
