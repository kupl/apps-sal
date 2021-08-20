input()
d = [0] * 2000000
for k in map(int, input().split()):
    d[k] = 1
for i in range(len(d)):
    d[i] = i if d[i] else d[i - 1]
m = 0
for i in range(999999, 0, -1):
    if d[i] == i and i > m + 1:
        m = max(m, max((j % i for j in d[2 * i - 1::i])))
print(m)
