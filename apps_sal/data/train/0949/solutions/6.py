import sys


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def get_list():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_string():
    return sys.stdin.readline().strip()


def helper(arr, s, n):
    ans = 0
    i = s
    while i < n:
        if i + 1 < n and arr[i] == arr[i + 1]:
            ans += 1
            i += 1
        elif i + 2 < n and arr[i] == arr[i + 2]:
            ans += 1
            i += 2
        else:
            break
    return ans


for _ in range(int(input())):
    n = int(input())
    arr = get_list()
    ans = 0
    for i in range(n):
        ans = max(ans, helper(arr, i, n))
    print(ans)
