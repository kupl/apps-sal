import random


def count_lens(t):
    t = list(t)
    n = len(t)
    res = 0
    for _ in range(n):
        for k in range(n - 1):
            if t[k] > t[k + 1]:
                t[k], t[k + 1] = t[k + 1], t[k]
                res += 1

    return (res) % 2


def prog():
    input()
    a, b = input(), input()
    if sorted(a) != sorted(b):
        print("NO")
        return

    if len(set(a)) < len(a):
        print("YES")
        return

    print("YES" if count_lens(a) == count_lens(b) else "NO")


t = int(input())
for _ in range(t):
    prog()
