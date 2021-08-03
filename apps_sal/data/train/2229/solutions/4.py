#!/usr/bin/env python3
# -*- coding = 'utf-8' -*-

t = input()
p = input()
a = list(map(int, input().split()))


def can(s, p):
    i = 0
    for ch in s:
        if ch == p[i]:
            i += 1
            if i == len(p):
                return True

    return False


def binary_search(l, r):

    while(l < r - 1):
        s = list(t)
        mid = (l + r) // 2

        for index in range(mid):
            s[a[index] - 1] = ' '

        ok = False
        i = 0
        for ch in s:
            if ch == p[i]:
                i += 1
                if i == len(p):
                    ok = True
                    break
        if ok:
            l = mid
        else:
            r = mid

    return l


print(binary_search(0, len(a) + 1))
