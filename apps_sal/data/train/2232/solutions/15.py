a = 2
n = 0
max = int(input())
for k in range(max + 1):
    if k == 0:
        continue
    n = k * (k + 1) * (k + 1) - a
    a = k
    print(n)
