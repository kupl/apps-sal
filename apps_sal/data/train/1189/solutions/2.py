import random


def abc(l, val):
    i = 0
    j = len(l) - 1
    s = -1
    while i <= j:
        mid = i + (j - i) // 2
        if l[mid] < val:
            s = mid
            i = mid + 1
        else:
            j = mid - 1
    return s + 1


def bca(l, val):
    i = 0
    j = len(l) - 1
    s = len(l)
    while i <= j:
        mid = i + (j - i) // 2
        if l[mid] >= val:
            s = mid
            j = mid - 1
        else:
            i = mid + 1
    m = 0
    return len(l) - s


t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    x = sum(l)
    ans = 0
    k = [l[0]]
    for i in range(1, n):
        k.append(k[-1] + l[i])
    d = {}
    for i in range(n):
        try:
            d[k[i]] += [i]
        except:
            d[k[i]] = [i]
    for i in range(n):
        s = x - l[i]
        if not s % 2:
            try:
                c = d[s // 2]
                ans += abc(c, i)
            except:
                pass
            try:
                c = d[s // 2 + l[i]]
                ans += bca(c, i)
                if k[-1] == s // 2 + l[i]:
                    ans -= 1
            except:
                pass
    print(ans)
