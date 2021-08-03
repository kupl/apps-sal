import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    rm = n
    not_rm = False
    ok = True
    for x in p:
        if not not_rm:
            if x == rm:
                rm -= 1
            else:
                not_rm = True
                last = x
                lm = x
        else:
            if x != last + 1:
                ok = False
                break
            elif x == rm:
                not_rm = False
                rm = lm - 1
            else:
                last = x
    if ok:
        print("Yes")
    else:
        print("No")
