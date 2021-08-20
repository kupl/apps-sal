import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
party = [[] for _ in range(m + 5)]
pc = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])
choose = [0] * n
for i in range(n):
    party[pc[i][0]].append(i)
want = 10 ** 18
for i in range(1, n + 1):
    p1 = len(party[1])
    for j in range(2, m + 5):
        if len(party[j]) < i:
            continue
        for k in range(len(party[j]) - i + 1):
            p1 += 1
            choose[party[j][k]] = 1
    want2 = 0
    for j in range(n):
        if p1 < i and choose[j] == 0 and (pc[j][0] != 1):
            choose[j] = 1
            p1 += 1
        if choose[j] == 1:
            want2 += pc[j][1]
    if want > want2:
        want = want2
    choose = [0] * n
print(want)
