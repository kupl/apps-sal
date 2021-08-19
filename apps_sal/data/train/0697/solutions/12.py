# cook your dish here
import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_list_string(): return list(map(str, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_print_int(x): sys.stdout.write(str(x) + '\n')
def get_print(x): sys.stdout.write(x + '\n')


def solve():
    for _ in range(get_int()):
        n, k = get_ints()
        arr = get_list()
        pre = 0
        s = 0
        for i in range(k):
            pre += arr[i]
        ans = pre
        for i in range(k, n, 1):
            pre = pre + arr[i] - arr[s]
            s += 1
            ans = max(ans, pre)
        get_print_int(ans)


solve()
