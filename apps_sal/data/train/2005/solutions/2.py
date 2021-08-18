from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


s = li()
n = len(s)
total = 0


def testsub(sub):
    for k in range(1, (len(sub) - 1) // 2 + 1):
        if sub[0] == sub[k] and sub[k] == sub[2 * k]:
            return True

    return False


for i in range(len(s)):
    r = n
    lets = 3

    done = 0
    while i + lets <= len(s):

        sli = s[i:i + lets]
        for m in range(0, len(sli) - 2):
            if testsub(sli[m:]):
                done = 1
                break
        if done == 1:
            r = i + len(sli) - 1
            break

        lets += 1
    total += n - r


print(total)
