import itertools
(N, X, Y) = list(map(int, input().split()))
contests = []
for _ in range(N):
    contests.append(list(map(int, input().split())))
into = list(map(int, input().split()))
outo = list(map(int, input().split()))
worthwole = [(x, y) for (x, y) in itertools.product(into, outo) if x < y]
worthwole = sorted(worthwole, key=lambda x: x[1] - x[0])
result = 0
found = False
for w in worthwole:
    for c in contests:
        if w[0] <= c[0] and w[1] >= c[1]:
            result = w[1] - w[0] + 1
            found = True
            break
    if found:
        break
print(result)
