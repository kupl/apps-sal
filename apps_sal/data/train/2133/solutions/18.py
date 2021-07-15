n = int(input())
l = [input() for _ in range(n)]
res = 0
for day in range(7):
    here = 0
    for i in range(n):
        if l[i][day] == '1':
            here += 1
    res = max(res, here)
print(res)
