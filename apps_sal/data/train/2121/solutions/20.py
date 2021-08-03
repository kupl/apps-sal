import sys


def sol(a, n):
    a.sort()
    i = 0
    j = n // 2
    ans = n
    while i < n // 2 and j < n:
        if 2 * a[i] <= a[j]:
            ans -= 1
            i += 1
            j += 1
        else:
            j += 1
    return ans


n = int(input())
a = [int(i) for i in sys.stdin]
print(sol(a, n))
