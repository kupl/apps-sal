import sys
from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    p, q = map(int, stdin.readline().split())

    if p % q != 0:
        print(p)
        continue

    bk = {}
    for i in range(2, 10**5):
        if q % i == 0:
            bk[i] = 0
            while q % i == 0:
                bk[i] += 1
                q //= i
        if bk == 1:
            break

    if q != 1:
        bk[q] = 1

    ans = float("-inf")
    for i in bk:
        cnt = 0
        tp = p
        while tp % i == 0:
            tp //= i
            cnt += 1
        ans = max(ans, p // (i**(cnt - bk[i] + 1)))

    print(ans)
