import sys


def minshift(s):
    s += s
    n = len(s)
    i, ans = 0, 0
    while i < n // 2:
        ans = i
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            if s[k] < s[j]:
                k = i
            else:
                k += 1
            j += 1

        while i <= k:
            i += j - k

    return s[ans:ans + n // 2]


t = int(sys.stdin.readline().strip())
for _ in range(t):
    l, s = sys.stdin.readline().strip().split()
    l = int(l)

    arr = [0] * len(s)
    for i in range(len(s)):
        arr[i] = s[i]

    if l >= 2:
        arr.sort()
        print(*arr, sep='')
        print('')
    else:
        print(minshift(s))
