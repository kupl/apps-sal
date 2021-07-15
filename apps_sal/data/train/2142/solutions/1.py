n = int(input())
p = [0] * n
for i in range(n):
    t = list(map(int, input().split()))
    t.pop(i)
    s = 0
    for j in t:
        s |= j
    p[i] = s
print(' '.join(map(str, p)))
