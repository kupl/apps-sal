n = int(input())
lst = list(map(int, input().split()))
d = dict()
sm = 0
for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    if d[i] % 2 == 0:
        sm += d[i] // 2
    else:
        sm += (d[i] + 1) // 2
print(sm)
