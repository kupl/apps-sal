import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

IN = [0] * n
OUT = [0] * n

INSET = [[] for i in range(n)]

for i in range(m):
    x, y = sorted(map(int, input().split()))

    IN[x - 1] += 1
    OUT[y - 1] += 1
    INSET[x - 1].append(y - 1)

ANS = 0
for i in range(n):
    ANS += IN[i] * OUT[i]

print(ANS)

Q = int(input())

for i in range(Q):
    q = int(input()) - 1
    ANS -= IN[q] * OUT[q]
    OUT[q] += IN[q]
    IN[q] = 0

    for x in INSET[q]:
        INSET[x].append(q)
        ANS += (IN[x] + 1) * (OUT[x] - 1) - IN[x] * OUT[x]
        IN[x] += 1
        OUT[x] -= 1

    INSET[q] = []

    print(ANS)
